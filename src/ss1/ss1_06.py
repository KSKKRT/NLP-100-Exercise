from ss1_05 import ngram

if __name__ == '__main__':
    s1: str = 'paraparaparadise'
    s2: str = 'paragraph'
    X: set = ngram(2, s1)
    Y: set = ngram(2, s2)
    print('union: ', X | Y)
    print('intersection: ', X & Y)
    print('subtraction: ', X - Y)
    se: set = ngram(2, 'se')
    print('se in X' if se <= X else 'se not in X')
    print('se in Y' if se <= Y else 'se not in Y')
    