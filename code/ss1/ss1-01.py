s = 'パタトクカシーー'

def extract_odd(str: s) -> str:
    return ''.join(list(s)[::2])

if __name__ == '__main__':
    print(extract_odd(s))