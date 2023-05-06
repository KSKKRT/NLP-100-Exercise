def ngram(n: int, s: tuple[str, list]) -> set:
    """
    To get character n-gram: input s
    To get word n-gram: input str.split()
    ex.
    s = 'I am 23'
    1. ngram(2, s) -> {('I', ' '), (' ', 'a'), ('a', 'm'), ('m', ' '), (' ', '2'), ('2', '3')}
    2. ngram(2, s.split()) -> {('I', 'am'),('am', '23')}
    """
    subwords: list = [s[i:] for i in range(n)]
    return set(zip(*subwords))

if __name__ == '__main__':
    s: str = 'I am 23'
    print('character bi-gram', ngram(2, s))
    print('word bi-gram', ngram(2,s.split()))
    