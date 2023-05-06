def cipher(s: str) -> str:
    cipher_list: list = [chr(219 - ord(c)) if c.islower() else c for c in s]
    return ''.join(cipher_list)

if __name__ == '__main__':
    s: str = '<BOS>It is a plaintext.<EOS>'
    enc: str = cipher(s)
    print('encryption: ', enc)
    dec: str = cipher(enc)
    print('decryption: ', dec)
    