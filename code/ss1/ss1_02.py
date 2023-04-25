def alter_concat(s1: str, s2: str) -> str:
    concat_text: str = ''
    for c1, c2 in zip(s1, s2):
        concat_text += (c1 + c2)
    return concat_text

if __name__ == '__main__':
    s1: str = 'パトカー'
    s2: str = 'タクシー'
    print(alter_concat(s1, s2))