def extract_odd(s: str) -> str:
    return ''.join(list(s)[::2])

if __name__ == '__main__':
    s = 'パタトクカシーー'
    print(extract_odd(s))