def longestPalindromicSubstring(string):
    left = 0
    right = 1
    for i in range(1, len(string)):
        odd_left, odd_right = get_palindromic(string, i - 1, i + 1)
        current_length = right - left
        if odd_right - odd_left > current_length:
            left = odd_left
            right = odd_right

        even_left, even_right = get_palindromic(string, i - 1, i)
        current_length = right - left
        if even_right - even_left > current_length:
            left = even_left
            right = even_right
    return string[left:right]


def get_palindromic(string, left, right):
    while 0 <= left and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return [left + 1, right]
