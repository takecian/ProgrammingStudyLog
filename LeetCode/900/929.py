# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local = email[:email.find('@')]
            domain = email[email.find('@'):]
            local = local.replace('.', '')
            if '+' in local:
                local = local[:local.find('+')]
            ans.add(local + domain)

        return len(ans)