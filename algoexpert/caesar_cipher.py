def caesarCipherEncryptor(string, key):
    # Write your code here.
    codes = list(map(lambda c: ord(c) - ord('a'), string))
    encrypted = list(map(lambda c: (c + key) % 26, codes))

    return ''.join(list(map(lambda c: chr(c + ord('a')), encrypted)))