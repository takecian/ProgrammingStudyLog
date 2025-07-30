#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import json
import getpass
import argparse
import datetime
import requests
import traceback
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Selenium imports
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False


class MixiDiaryExporter:
    """
    A class to export diary entries from mixi.jp
    """
    
    BASE_URL = "https://mixi.jp"
    LOGIN_URL = "https://mixi.jp/home.pl"
    DIARY_LIST_URL = "https://mixi.jp/list_diary.pl"
    
    def __init__(self, email=None, password=None, cookie_str=None, output_dir="mixi_diaries", debug=False, use_selenium=True):
        """
        Initialize the exporter with login credentials and output directory
        
        Args:
            email (str): mixi login email
            password (str): mixi login password
            cookie_str (str): cookie string for authentication (alternative to email/password)
            output_dir (str): directory to save exported diaries
            debug (bool): enable debug mode
            use_selenium (bool): use Selenium for web scraping
        """
        self.email = email
        self.password = password
        self.cookie_str = cookie_str
        self.output_dir = output_dir
        self.debug = debug
        self.use_selenium = use_selenium and SELENIUM_AVAILABLE
        
        # Initialize requests session for non-Selenium operations
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
            'Referer': 'https://mixi.jp/',
            'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        })
        
        # Set cookies if provided
        if self.cookie_str:
            self._set_cookies(self.cookie_str)
        
        # Initialize Selenium WebDriver if available
        self.driver = None
        if self.use_selenium:
            try:
                self._init_selenium()
            except Exception as e:
                print(f"Error initializing Selenium: {e}")
                self.use_selenium = False
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")
            
        # Create subdirectories for different formats
        self.html_dir = os.path.join(output_dir, "html")
        self.json_dir = os.path.join(output_dir, "json")
        self.text_dir = os.path.join(output_dir, "text")
        
        for directory in [self.html_dir, self.json_dir, self.text_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)
    
    def debug_print(self, message, save_html=False, html_content=None, filename=None):
        """
        Print debug information if debug mode is enabled
        
        Args:
            message (str): Debug message to print
            save_html (bool): Whether to save HTML content to a file
            html_content (str): HTML content to save
            filename (str): Filename to save HTML content to
        """
        if self.debug:
            print(f"[DEBUG] {message}")
            
            if save_html and html_content:
                debug_dir = os.path.join(self.output_dir, "debug")
                if not os.path.exists(debug_dir):
                    os.makedirs(debug_dir)
                
                if not filename:
                    filename = f"debug_{int(time.time())}.html"
                
                debug_file = os.path.join(debug_dir, filename)
                with open(debug_file, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                print(f"[DEBUG] Saved HTML content to {debug_file}")
    
    def _init_selenium(self):
        """
        Initialize Selenium WebDriver
        """
        if not SELENIUM_AVAILABLE:
            print("Selenium is not available. Please install it with: pip install selenium")
            return False
        
        try:
            # Set up Chrome options
            chrome_options = Options()
            if not self.debug:
                chrome_options.add_argument("--headless")  # Run in headless mode if not debugging
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            
            # Add user agent
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
            
            # Initialize the WebDriver
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_page_load_timeout(30)
            
            self.debug_print("Selenium WebDriver initialized successfully")
            return True
        except Exception as e:
            print(f"Failed to initialize Selenium WebDriver: {e}")
            self.debug_print(f"Selenium initialization error: {traceback.format_exc()}")
            return False
    
    def _set_cookies(self, cookie_str):
        """
        Set cookies from a cookie string
        
        Args:
            cookie_str (str): Cookie string in the format "name1=value1; name2=value2; ..."
        """
        # Parse cookie string and set cookies in the requests session
        if cookie_str:
            print("Setting cookies from provided cookie string...")
            cookie_pairs = cookie_str.split(';')
            for pair in cookie_pairs:
                if '=' in pair:
                    name, value = pair.strip().split('=', 1)
                    self.session.cookies.set(name, value, domain='.mixi.jp')
                    self.debug_print(f"Set cookie: {name}={value}")
        
        # If using Selenium, also set cookies in the browser
        if self.use_selenium and self.driver:
            # First navigate to the domain
            self.driver.get(self.BASE_URL)
            time.sleep(1)
            
            # Then set cookies
            for cookie in self.session.cookies:
                if cookie.domain and '.mixi.jp' in cookie.domain:
                    cookie_dict = {
                        'name': cookie.name,
                        'value': cookie.value,
                        'domain': cookie.domain
                    }
                    try:
                        self.driver.add_cookie(cookie_dict)
                        self.debug_print(f"Set Selenium cookie: {cookie.name}={cookie.value}")
                    except Exception as e:
                        self.debug_print(f"Error setting Selenium cookie {cookie.name}: {e}")
    
    def login(self):
        """
        Log in to mixi using the provided credentials or cookies
        
        Returns:
            bool: True if login successful, False otherwise
        """
        print("Logging in to mixi.jp...")
        
        # If we have cookies, verify they work by checking if we can access the diary list
        if self.cookie_str:
            print("Using provided cookies for authentication...")
            try:
                # Try to access the diary list page
                response = self.session.get(self.DIARY_LIST_URL)
                response.raise_for_status()
                
                # Check if we're logged in
                success_indicators = ["ログアウト", "logout", "マイミク", "ホーム", "home", "my mixi"]
                for indicator in success_indicators:
                    if indicator in response.text.lower():
                        print("Login successful with cookies!")
                        return True
                
                print("Cookies are invalid or expired. Falling back to credentials...")
            except Exception as e:
                print(f"Error verifying cookies: {e}")
                print("Falling back to credentials...")
        
        # If cookies didn't work or weren't provided, use credentials
        if self.email and self.password:
            if self.use_selenium:
                return self._login_with_selenium()
            else:
                return self._login_with_requests()
        else:
            print("No valid authentication method available. Please provide either cookies or email/password.")
            return False
    
    def _login_with_selenium(self):
        """
        Log in to mixi using Selenium
        
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            # Navigate to the login page
            self.driver.get(self.LOGIN_URL)
            
            # Save the login page HTML for debugging
            self.debug_print("Got login page with Selenium", save_html=True, 
                            html_content=self.driver.page_source, filename="login_page_selenium.html")
            
            # Print all forms for debugging
            try:
                forms = self.driver.find_elements(By.TAG_NAME, "form")
                self.debug_print(f"Found {len(forms)} forms on the page")
                for i, form in enumerate(forms):
                    self.debug_print(f"Form {i+1} action: {form.get_attribute('action')}")
                    self.debug_print(f"Form {i+1} class: {form.get_attribute('class')}")
                    self.debug_print(f"Form {i+1} data-widget-namespace: {form.get_attribute('data-widget-namespace')}")
            except Exception as e:
                self.debug_print(f"Error listing forms: {e}")
            
            # Try to find the login form directly using the exact structure from the provided HTML
            try:
                # First try to find the outer container
                login_form_container = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".PORTAL_loginForm__inner"))
                )
                self.debug_print("Found .PORTAL_loginForm__inner container")
                
                # Then find the form inside it
                form = login_form_container.find_element(By.TAG_NAME, "form")
                self.debug_print(f"Found form inside .PORTAL_loginForm__inner with action: {form.get_attribute('action')}")
            except (TimeoutException, NoSuchElementException) as e:
                self.debug_print(f"Could not find .PORTAL_loginForm__inner container: {e}")
                
                # Try to find the form directly by its action and data attribute
                try:
                    form = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "form[action*='login.pl'][data-widget-namespace='jp.mixi.ui.form.widget.recaptcha.v3']"))
                    )
                    self.debug_print("Found form by action and data-widget-namespace")
                except TimeoutException:
                    # Try just by action
                    try:
                        form = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "form[action*='login.pl']"))
                        )
                        self.debug_print("Found form by action")
                    except TimeoutException:
                        # Last resort: try to find any form
                        try:
                            form = WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located((By.TAG_NAME, "form"))
                            )
                            self.debug_print(f"Found form by tag name with action: {form.get_attribute('action')}")
                        except TimeoutException:
                            print("Error: Could not find any form")
                            self.debug_print("No form found", save_html=True, 
                                            html_content=self.driver.page_source, filename="no_form_found.html")
                            return False
            
            # Now find the email and password fields within the form
            try:
                # Try to find email field
                email_field = form.find_element(By.NAME, "email")
                self.debug_print("Found email field by name")
            except NoSuchElementException:
                # Try alternative selectors
                try:
                    email_field = form.find_element(By.CSS_SELECTOR, ".PORTAL_loginForm__inputText[name='email']")
                    self.debug_print("Found email field by class and name")
                except NoSuchElementException:
                    try:
                        email_field = form.find_element(By.CSS_SELECTOR, "input[type='text']")
                        self.debug_print("Found email field by input type")
                    except NoSuchElementException:
                        print("Error: Could not find email field")
                        self.debug_print("Email field not found", save_html=True, 
                                        html_content=self.driver.page_source, filename="email_field_not_found.html")
                        return False
            
            try:
                # Try to find password field
                password_field = form.find_element(By.NAME, "password")
                self.debug_print("Found password field by name")
            except NoSuchElementException:
                try:
                    password_field = form.find_element(By.CSS_SELECTOR, "input[type='password']")
                    self.debug_print("Found password field by type")
                except NoSuchElementException:
                    print("Error: Could not find password field")
                    self.debug_print("Password field not found", save_html=True, 
                                    html_content=self.driver.page_source, filename="password_field_not_found.html")
                    return False
            
            # Enter credentials
            email_field.clear()
            email_field.send_keys(self.email)
            self.debug_print(f"Entered email: {self.email}")
            
            password_field.clear()
            password_field.send_keys(self.password)
            self.debug_print("Entered password")
            
            # Find the login button
            try:
                # Try to find by specific class
                login_button = form.find_element(By.CSS_SELECTOR, ".PORTAL_loginForm__button--gold")
                self.debug_print("Found login button by specific class")
            except NoSuchElementException:
                try:
                    # Try by input type submit
                    login_button = form.find_element(By.CSS_SELECTOR, "input[type='submit']")
                    self.debug_print("Found login button by input type")
                except NoSuchElementException:
                    try:
                        # Try by button type
                        login_button = form.find_element(By.CSS_SELECTOR, "button[type='submit']")
                        self.debug_print("Found login button by button type")
                    except NoSuchElementException:
                        print("Error: Could not find login button")
                        self.debug_print("Login button not found", save_html=True, 
                                        html_content=self.driver.page_source, filename="login_button_not_found.html")
                        return False
            
            # Handle reCAPTCHA v3 if present
            if form.get_attribute('data-widget-namespace') == 'jp.mixi.ui.form.widget.recaptcha.v3':
                self.debug_print("Form has reCAPTCHA v3, waiting for token generation")
                # The site likely handles reCAPTCHA v3 via JavaScript, so we just need to wait a bit
                time.sleep(3)
            
            # Click the login button
            self.debug_print("Clicking login button")
            login_button.click()
            
            # Wait for the page to load after login
            time.sleep(5)
            
            # Save the response HTML for debugging
            self.debug_print("Got login response with Selenium", save_html=True, 
                            html_content=self.driver.page_source, filename="login_response_selenium.html")
            
            # Check if login was successful
            success_indicators = ["ログアウト", "logout", "マイミク", "ホーム", "home", "my mixi"]
            page_source_lower = self.driver.page_source.lower()
            
            for indicator in success_indicators:
                if indicator.lower() in page_source_lower:
                    print("Login successful!")
                    return True
            
            print("Login failed. Please check your credentials.")
            return False
            
        except Exception as e:
            print(f"Error during Selenium login: {e}")
            self.debug_print(f"Selenium login error traceback: {traceback.format_exc()}")
            return False
    
    def _login_with_requests(self):
        """
        Log in to mixi using requests (fallback method)
        
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            login_page = self.session.get(self.LOGIN_URL)
            login_page.raise_for_status()
            
            # Save the login page HTML for debugging
            self.debug_print("Got login page with requests", save_html=True, 
                            html_content=login_page.text, filename="login_page_requests.html")
            
            soup = BeautifulSoup(login_page.text, 'html.parser')
            
            # Print all forms for debugging
            forms = soup.find_all('form')
            self.debug_print(f"Found {len(forms)} forms on the page")
            for i, f in enumerate(forms):
                self.debug_print(f"Form {i+1} action: {f.get('action')}")
                self.debug_print(f"Form {i+1} class: {f.get('class')}")
                self.debug_print(f"Form {i+1} data-widget-namespace: {f.get('data-widget-namespace')}")
            
            # Try to find the login form using the specific structure from the provided HTML
            login_form_container = soup.select_one('.PORTAL_loginForm__inner')
            if login_form_container:
                self.debug_print("Found .PORTAL_loginForm__inner container")
                form = login_form_container.find('form')
                if form:
                    self.debug_print(f"Found form inside .PORTAL_loginForm__inner with action: {form.get('action')}")
                else:
                    self.debug_print("No form found inside .PORTAL_loginForm__inner")
                    form = None
            else:
                self.debug_print("Could not find .PORTAL_loginForm__inner container")
                form = None
            
            # If not found, try other selectors
            if not form:
                selectors = [
                    {'action': re.compile(r'login.pl'), 'data-widget-namespace': re.compile(r'jp\.mixi\.ui\.form\.widget\.recaptcha\.v3')},
                    {'action': re.compile(r'login.pl')},
                    {'data-widget-namespace': re.compile(r'jp\.mixi\.ui\.form\.widget\.recaptcha\.v3')},
                    {'id': 'login_form'},
                    {'class_': 'loginForm'},
                    {'method': 'post'}
                ]
                
                for selector in selectors:
                    form = soup.find('form', selector)
                    if form:
                        self.debug_print(f"Found form with selector: {selector}")
                        break
            
            if not form:
                # Try to find any form
                if forms:
                    form = forms[0]
                    self.debug_print(f"Using first form found (total forms: {len(forms)})")
                else:
                    print("Error: Could not find any login form")
                    return False
            
            # Find the form action URL
            action_url = form.get('action', self.LOGIN_URL)
            if not action_url.startswith('http'):
                action_url = urljoin(self.BASE_URL, action_url)
            
            self.debug_print(f"Form action URL: {action_url}")
            
            # Check if the form has reCAPTCHA v3 attributes
            has_recaptcha = form.get('data-widget-namespace') == 'jp.mixi.ui.form.widget.recaptcha.v3'
            recaptcha_token_field = form.get('data-token-field-name', 'recaptcha_v3_token')
            recaptcha_action = form.get('data-action-name', 'login')
            
            if has_recaptcha:
                self.debug_print(f"Form has reCAPTCHA v3. Token field: {recaptcha_token_field}, Action: {recaptcha_action}")
            
            # Find input field names - use the specific classes from the provided HTML first
            email_field = None
            password_field = None
            
            # Try to find email field with the specific class
            email_input = form.select_one('.PORTAL_loginForm__inputText[name="email"]')
            if email_input and email_input.get('name'):
                email_field = email_input['name']
                self.debug_print(f"Found email field with specific class: {email_field}")
            
            # Try to find password field
            password_input = form.select_one('input[name="password"]')
            if password_input and password_input.get('name'):
                password_field = password_input['name']
                self.debug_print(f"Found password field: {password_field}")
            
            # If we couldn't find the fields with specific selectors, try more generic approaches
            if not email_field:
                # Try common email/username field names
                for field in ['email', 'username', 'user', 'account', 'id', 'mail']:
                    input_field = form.find('input', {'name': field}) or form.find('input', {'id': field})
                    if input_field:
                        email_field = field
                        self.debug_print(f"Found email field: {email_field}")
                        break
                
                # If still not found, try to infer from input types
                if not email_field:
                    email_input = form.find('input', {'type': 'email'}) or form.find('input', {'type': 'text'})
                    if email_input and email_input.get('name'):
                        email_field = email_input['name']
                        self.debug_print(f"Inferred email field from input type: {email_field}")
            
            if not password_field:
                # Try common password field names
                for field in ['password', 'pass', 'pwd']:
                    input_field = form.find('input', {'name': field}) or form.find('input', {'id': field})
                    if input_field:
                        password_field = field
                        self.debug_print(f"Found password field: {password_field}")
                        break
                
                # If still not found, try to infer from input types
                if not password_field:
                    password_input = form.find('input', {'type': 'password'})
                    if password_input and password_input.get('name'):
                        password_field = password_input['name']
                        self.debug_print(f"Inferred password field from input type: {password_field}")
            
            # If we still couldn't find the field names, use defaults
            if not email_field:
                email_field = 'email'
                self.debug_print(f"Using default email field: {email_field}")
            
            if not password_field:
                password_field = 'password'
                self.debug_print(f"Using default password field: {password_field}")
            
            # Prepare login data
            login_data = {
                email_field: self.email,
                password_field: self.password,
            }
            
            # Add any hidden fields from the form
            for hidden_input in form.find_all('input', {'type': 'hidden'}):
                if hidden_input.get('name'):
                    login_data[hidden_input['name']] = hidden_input.get('value', '')
                    self.debug_print(f"Added hidden field: {hidden_input['name']} = {hidden_input.get('value', '')}")
            
            # Add common next_url field if not present
            if 'next_url' not in login_data:
                login_data['next_url'] = '/'
            
            # Handle reCAPTCHA v3 if present
            if has_recaptcha:
                # For reCAPTCHA v3, we would normally need to execute JavaScript to get a token
                # Since we can't do that with requests, we'll add an empty token and hope the server accepts it
                # In a real-world scenario, you might need to use a service to solve reCAPTCHA
                login_data[recaptcha_token_field] = ''
                self.debug_print(f"Added empty reCAPTCHA v3 token field: {recaptcha_token_field}")
            
            self.debug_print(f"Login data: {login_data}")
            
            # Submit login form
            response = self.session.post(action_url, data=login_data)
            response.raise_for_status()
            
            # Save the response HTML for debugging
            self.debug_print("Got login response with requests", save_html=True, 
                            html_content=response.text, filename="login_response_requests.html")
            
            # Check if login was successful
            success_indicators = ["ログアウト", "logout", "マイミク", "ホーム", "home", "my mixi"]
            for indicator in success_indicators:
                if indicator in response.text.lower():
                    print("Login successful!")
                    return True
            
            print("Login failed. Please check your credentials.")
            return False
            
        except Exception as e:
            print(f"Error during requests login: {e}")
            self.debug_print(f"Requests login error traceback: {traceback.format_exc()}")
            return False
    
    def get_diary_list_pages(self):
        """
        Get all diary list pages
        
        Returns:
            list: List of URLs for all diary pages
        """
        print("Getting diary list pages...")
        
        if self.use_selenium:
            return self._get_diary_list_pages_with_selenium()
        else:
            return self._get_diary_list_pages_with_requests()
    
    def _get_diary_list_pages_with_selenium(self):
        """
        Get all diary list pages using Selenium
        
        Returns:
            list: List of URLs for all diary pages
        """
        diary_urls = []
        page = 1
        has_next = True
        
        try:
            while has_next:
                print(f"Processing diary list page {page} with Selenium...")
                url = f"{self.DIARY_LIST_URL}?page={page}"
                
                self.driver.get(url)
                time.sleep(3)  # Wait for the page to load
                
                # Save the page HTML for debugging
                self.debug_print(f"Got diary list page {page}", save_html=True, 
                                html_content=self.driver.page_source, filename=f"diary_list_page_{page}_selenium.html")
                
                # Find all diary entry links
                diary_entries = self.driver.find_elements(By.CSS_SELECTOR, 'div.listDiaryTitle a')
                
                if not diary_entries:
                    print(f"No diary entries found on page {page}")
                    break
                
                # Extract diary URLs
                for entry in diary_entries:
                    diary_url = entry.get_attribute('href')
                    diary_urls.append(diary_url)
                
                # Check if there's a next page
                try:
                    next_link = self.driver.find_element(By.CSS_SELECTOR, 'a.nextPage')
                    has_next = True
                except NoSuchElementException:
                    has_next = False
                
                page += 1
                
                # Add a small delay to avoid rate limiting
                time.sleep(1)
            
            print(f"Found {len(diary_urls)} diary entries with Selenium")
            return diary_urls
            
        except Exception as e:
            print(f"Error getting diary list pages with Selenium: {e}")
            self.debug_print(f"Selenium diary list error traceback: {traceback.format_exc()}")
            return diary_urls
    
    def _get_diary_list_pages_with_requests(self):
        """
        Get all diary list pages using requests
        
        Returns:
            list: List of URLs for all diary pages
        """
        diary_urls = []
        page = 1
        has_next = True
        
        try:
            while has_next:
                print(f"Processing diary list page {page} with requests...")
                url = f"{self.DIARY_LIST_URL}?page={page}"
                response = self.session.get(url)
                
                # Save the page HTML for debugging
                self.debug_print(f"Got diary list page {page}", save_html=True, 
                                html_content=response.text, filename=f"diary_list_page_{page}_requests.html")
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all diary entry links
                diary_entries = soup.select('div.listDiaryTitle a')
                if not diary_entries:
                    print(f"No diary entries found on page {page}")
                    break
                
                # Extract diary URLs
                for entry in diary_entries:
                    diary_url = urljoin(self.BASE_URL, entry['href'])
                    if 'edit' not in diary_url:
                        diary_urls.append(diary_url)
                        print(f"Found diary URL: {diary_url}")
                
                # Check if there's a next page
                has_next = page < 35
                page += 1
                
                # Add a small delay to avoid rate limiting
                time.sleep(1)
            
            print(f"Found {len(diary_urls)} diary entries with requests")
            return diary_urls
            
        except Exception as e:
            print(f"Error getting diary list pages with requests: {e}")
            self.debug_print(f"Requests diary list error traceback: {traceback.format_exc()}")
            return diary_urls
    
    def extract_diary_content(self, url):
        """
        Extract content from a diary page
        
        Args:
            url (str): URL of the diary page
            
        Returns:
            dict: Diary entry data
        """
        print(f"Extracting content from {url}")
        
        if self.use_selenium:
            return self._extract_diary_content_with_selenium(url)
        else:
            return self._extract_diary_content_with_requests(url)
    
    def _extract_diary_content_with_selenium(self, url):
        """
        Extract content from a diary page using Selenium
        
        Args:
            url (str): URL of the diary page
            
        Returns:
            dict: Diary entry data
        """
        try:
            self.driver.get(url)
            time.sleep(3)  # Wait for the page to load
            
            # Save the page HTML for debugging
            self.debug_print(f"Got diary page {url}", save_html=True, 
                            html_content=self.driver.page_source, filename=f"diary_page_selenium_{int(time.time())}.html")
            
            # Extract diary ID from URL
            diary_id = re.search(r'id=(\d+)', url)
            diary_id = diary_id.group(1) if diary_id else "unknown"
            
            # Extract title
            title = "No Title"
            try:
                title_elem = self.driver.find_element(By.CSS_SELECTOR, 'div.diaryTitle h3')
                title = title_elem.text.strip()
            except NoSuchElementException:
                pass
            
            # Extract date
            date_str = ""
            date_iso = ""
            try:
                date_elem = self.driver.find_element(By.CSS_SELECTOR, 'div.diaryDate')
                date_str = date_elem.text.strip()
                
                # Parse Japanese date format (e.g., "2023年5月1日 12:34")
                date_match = re.search(r'(\d+)年(\d+)月(\d+)日\s+(\d+):(\d+)', date_str)
                if date_match:
                    year, month, day, hour, minute = map(int, date_match.groups())
                    date = datetime.datetime(year, month, day, hour, minute)
                    date_iso = date.isoformat()
            except (NoSuchElementException, Exception) as e:
                self.debug_print(f"Error parsing date: {e}")
            
            # Extract content
            content_html = "<div>No content</div>"
            content_text = "No content"
            try:
                content_elem = self.driver.find_element(By.CSS_SELECTOR, 'div.viewDiaryBox')
                content_html = content_elem.get_attribute('outerHTML')
                content_text = content_elem.text.strip()
            except NoSuchElementException:
                # Fallback to diaryContent if viewDiaryBox is not found
                try:
                    content_elem = self.driver.find_element(By.CSS_SELECTOR, 'div.diaryContent')
                    content_html = content_elem.get_attribute('outerHTML')
                    content_text = content_elem.text.strip()
                except NoSuchElementException:
                    pass
            
            # Extract images
            images = []
            try:
                img_elems = self.driver.find_elements(By.CSS_SELECTOR, 'div.viewDiaryBox img')
                for img in img_elems:
                    img_url = img.get_attribute('src')
                    if img_url:
                        img_url = urljoin(self.BASE_URL, img_url)
                        images.append(img_url)
            except Exception as e:
                self.debug_print(f"Error extracting images: {e}")
            
            # Create diary entry data
            diary_data = {
                'id': diary_id,
                'url': url,
                'title': title,
                'date': date_iso,
                'date_original': date_str,
                'content_text': content_text,
                'content_html': content_html,
                'images': images
            }
            
            return diary_data
            
        except Exception as e:
            print(f"Error extracting diary content with Selenium: {e}")
            self.debug_print(f"Selenium diary content error traceback: {traceback.format_exc()}")
            
            # Fallback to requests method
            print("Falling back to requests method...")
            return self._extract_diary_content_with_requests(url)
    
    def _extract_diary_content_with_requests(self, url):
        """
        Extract content from a diary page using requests
        
        Args:
            url (str): URL of the diary page
            
        Returns:
            dict: Diary entry data
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()
            
            # Save the page HTML for debugging
            self.debug_print(f"Got diary page {url}", save_html=True, 
                            html_content=response.text, filename=f"diary_page_requests_{int(time.time())}.html")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract diary ID from URL
            diary_id = re.search(r'id=(\d+)', url)
            diary_id = diary_id.group(1) if diary_id else "unknown"
            
            # Extract title
            title_elem = soup.select_one('div.diaryTitle h3')
            title = title_elem.text.strip() if title_elem else "No Title"
            
            # Extract date
            date_elem = soup.select_one('div.diaryDate')
            date_str = date_elem.text.strip() if date_elem else ""
            date_iso = ""
            try:
                # Parse Japanese date format (e.g., "2023年5月1日 12:34")
                date_match = re.search(r'(\d+)年(\d+)月(\d+)日\s+(\d+):(\d+)', date_str)
                if date_match:
                    year, month, day, hour, minute = map(int, date_match.groups())
                    date = datetime.datetime(year, month, day, hour, minute)
                    date_iso = date.isoformat()
            except Exception as e:
                self.debug_print(f"Error parsing date: {e}")
            
            # Extract content
            content_elem = soup.select_one('div.viewDiaryBox')
            if not content_elem:
                # Fallback to diaryContent if viewDiaryBox is not found
                content_elem = soup.select_one('div.diaryContent')
            
            content_html = str(content_elem) if content_elem else "<div>No content</div>"
            content_text = content_elem.text.strip() if content_elem else "No content"
            
            # Extract images
            images = []
            for img in soup.select('div.viewDiaryBox img'):
                if img.get('src'):
                    img_url = urljoin(self.BASE_URL, img['src'])
                    images.append(img_url)
            
            # Create diary entry data
            diary_data = {
                'id': diary_id,
                'url': url,
                'title': title,
                'date': date_iso,
                'date_original': date_str,
                'content_text': content_text,
                'content_html': content_html,
                'images': images
            }
            
            return diary_data
            
        except Exception as e:
            print(f"Error extracting diary content with requests: {e}")
            self.debug_print(f"Requests diary content error traceback: {traceback.format_exc()}")
            
            # Return empty diary data
            return {
                'id': "unknown",
                'url': url,
                'title': "Error",
                'date': "",
                'date_original': "",
                'content_text': f"Error extracting content: {str(e)}",
                'content_html': f"<div>Error extracting content: {str(e)}</div>",
                'images': []
            }
    
    def save_diary_entry(self, diary_data):
        """
        Save diary entry in multiple formats
        
        Args:
            diary_data (dict): Diary entry data
            
        Returns:
            bool: True if saved successfully, False otherwise
        """
        diary_id = diary_data['id']
        date_prefix = ""
        
        # Add date prefix to filename if available
        if diary_data['date']:
            date_obj = datetime.datetime.fromisoformat(diary_data['date'])
            date_prefix = date_obj.strftime('%Y%m%d_%H%M_')
        
        # Save as JSON
        json_path = os.path.join(self.json_dir, f"{date_prefix}{diary_id}.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(diary_data, f, ensure_ascii=False, indent=2)
        
        # Save as HTML - use date as filename if available, otherwise use diary ID
        if diary_data['date']:
            date_obj = datetime.datetime.fromisoformat(diary_data['date'])
            html_filename = date_obj.strftime('%Y%m%d_%H%M') + '.html'
        else:
            html_filename = f"{diary_id}.html"
        html_path = os.path.join(self.html_dir, html_filename)
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{diary_data['title']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .diary-title {{ font-size: 24px; margin-bottom: 10px; }}
        .diary-date {{ color: #666; margin-bottom: 20px; }}
        .diary-content {{ line-height: 1.6; }}
        .diary-footer {{ margin-top: 30px; color: #666; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="diary-title">{diary_data['title']}</div>
    <div class="diary-date">{diary_data['date_original']}</div>
    <div class="diary-content">{diary_data['content_html']}</div>
    <div class="diary-footer">
        <p>Exported from mixi.jp on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Original URL: <a href="{diary_data['url']}">{diary_data['url']}</a></p>
    </div>
</body>
</html>"""
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Save as text
        text_path = os.path.join(self.text_dir, f"{date_prefix}{diary_id}.txt")
        text_content = f"""Title: {diary_data['title']}
Date: {diary_data['date_original']}
URL: {diary_data['url']}

{diary_data['content_text']}

Images:
{chr(10).join(diary_data['images'])}

Exported from mixi.jp on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        print(f"Saved diary entry {diary_id} in multiple formats")
        return True
    
    def download_images(self, diary_data):
        """
        Download images from a diary entry
        
        Args:
            diary_data (dict): Diary entry data
            
        Returns:
            list: List of downloaded image paths
        """
        if not diary_data['images']:
            return []
        
        diary_id = diary_data['id']
        image_dir = os.path.join(self.output_dir, "images", diary_id)
        
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        
        downloaded_images = []
        for i, img_url in enumerate(diary_data['images']):
            try:
                # Extract file extension from URL or default to .jpg
                file_ext = os.path.splitext(img_url)[1]
                if not file_ext:
                    file_ext = '.jpg'
                
                img_path = os.path.join(image_dir, f"image_{i+1}{file_ext}")
                
                # Download image
                img_response = self.session.get(img_url, stream=True)
                img_response.raise_for_status()
                
                with open(img_path, 'wb') as f:
                    for chunk in img_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                downloaded_images.append(img_path)
                print(f"Downloaded image: {img_path}")
                
                # Add a small delay
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error downloading image {img_url}: {e}")
        
        return downloaded_images
    
    def export_all_diaries(self):
        """
        Export all diary entries
        
        Returns:
            bool: True if export successful, False otherwise
        """
        # Login to mixi
        if not self.login():
            return False
        
        # Get all diary URLs
        diary_urls = self.get_diary_list_pages()
        if not diary_urls:
            print("No diary entries found")
            return False
        
        # Process each diary entry
        total_entries = len(diary_urls)
        successful_exports = 0
        
        for i, url in enumerate(diary_urls):
            try:
                print(f"\nProcessing diary {i+1}/{total_entries}: {url}")
                
                # Extract diary content
                diary_data = self.extract_diary_content(url)
                
                # Save diary entry
                if self.save_diary_entry(diary_data):
                    successful_exports += 1
                
                # Download images
                self.download_images(diary_data)
                
                # Add a delay between requests
                time.sleep(1)
                
            except Exception as e:
                print(f"Error processing diary {url}: {e}")
        
        print(f"\nExport completed: {successful_exports}/{total_entries} entries exported successfully")
        print(f"Diaries saved to: {os.path.abspath(self.output_dir)}")
        
        # Create index.html file
        self.create_index_html()
        
        return successful_exports > 0
    
    def create_index_html(self):
        """
        Create an index.html file that lists all exported diaries
        """
        print("Creating index.html...")
        
        # Get all HTML files
        html_files = []
        for filename in os.listdir(self.html_dir):
            if filename.endswith('.html'):
                file_path = os.path.join(self.html_dir, filename)
                # Get file creation time for sorting
                ctime = os.path.getctime(file_path)
                html_files.append((filename, ctime, file_path))
        
        # Sort by filename (which includes date if available)
        html_files.sort(reverse=True)
        
        # Create index.html content
        index_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mixi Diary Export</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #333; }}
        .diary-list {{ margin-top: 20px; }}
        .diary-item {{ margin-bottom: 10px; padding: 10px; border-bottom: 1px solid #eee; }}
        .diary-item a {{ text-decoration: none; color: #0066cc; }}
        .diary-item a:hover {{ text-decoration: underline; }}
        .diary-date {{ color: #666; font-size: 14px; margin-left: 10px; }}
        .footer {{ margin-top: 30px; color: #666; font-size: 12px; }}
    </style>
</head>
<body>
    <h1>Mixi Diary Export</h1>
    <p>Total entries: {len(html_files)}</p>
    <p>Export date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    
    <div class="diary-list">
"""
        
        # Add entries to index
        for filename, _, file_path in html_files:
            try:
                # Extract title from HTML file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    title_match = re.search(r'<div class="diary-title">(.*?)</div>', content)
                    title = title_match.group(1) if title_match else filename
                    
                    date_match = re.search(r'<div class="diary-date">(.*?)</div>', content)
                    date = date_match.group(1) if date_match else ""
                
                rel_path = os.path.join("html", filename)
                index_content += f"""    <div class="diary-item">
        <a href="{rel_path}">{title}</a>
        <span class="diary-date">{date}</span>
    </div>
"""
            except Exception as e:
                print(f"Error processing {filename} for index: {e}")
                # Fallback to just filename
                rel_path = os.path.join("html", filename)
                index_content += f"""    <div class="diary-item">
        <a href="{rel_path}">{filename}</a>
    </div>
"""
        
        # Close HTML
        index_content += """    </div>
    
    <div class="footer">
        <p>Generated by mixi_diary_exporter.py</p>
    </div>
</body>
</html>"""
        
        # Write index.html
        index_path = os.path.join(self.output_dir, "index.html")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"Created index.html at {index_path}")


def main():
    """
    Main function to run the exporter
    """
    parser = argparse.ArgumentParser(description='Export diary entries from mixi.jp')
    parser.add_argument('-e', '--email', help='mixi login email')
    parser.add_argument('-p', '--password', help='mixi login password')
    parser.add_argument('-c', '--cookie', help='cookie string for authentication (alternative to email/password)')
    parser.add_argument('-o', '--output', default='mixi_diaries', help='output directory')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
    parser.add_argument('-s', '--selenium', action='store_true', help='use Selenium for web scraping')
    args = parser.parse_args()
    
    # Check if cookie is provided
    if args.cookie:
        cookie_str = args.cookie
        email = None
        password = None
    else:
        cookie_str = None
        # Get credentials if not provided
        email = args.email
        password = args.password
        
        if not email:
            email = input("Enter your mixi email: ")
        
        if not password:
            password = getpass.getpass("Enter your mixi password: ")
    
    # Create exporter and run
    exporter = MixiDiaryExporter(
        email=email, 
        password=password,
        cookie_str=cookie_str,
        output_dir=args.output, 
        debug=args.debug,
        use_selenium=args.selenium
    )
    success = exporter.export_all_diaries()
    
    if success:
        print("\nDiary export completed successfully!")
        print(f"You can view your diaries by opening: {os.path.abspath(os.path.join(args.output, 'index.html'))}")
    else:
        print("\nDiary export failed.")


if __name__ == "__main__":
    main()
