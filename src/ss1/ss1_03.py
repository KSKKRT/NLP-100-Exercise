import re

def pi(s: str) -> list:
    s = re.sub('[.,]', '', s)
    words = s.split()
    return list(map(lambda word: len(word), words))


if __name__ == '__main__':
    s: str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    
    print(pi(s))