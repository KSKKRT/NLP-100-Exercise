def element_symbol(s: str) -> dict:
    s = s.replace('.', '')
    words: list = s.split()
    one_extract_idx: list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    result: dict = {}
    for i in range(len(words)):
        word: str = words[i]
        if i+1 in one_extract_idx:
            result[i+1] = word[:1]
        else:
            result[i+1] = word[:2]
    return result
    
if __name__ == '__main__':
    s: str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    
    print(element_symbol(s))