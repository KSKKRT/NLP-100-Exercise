import random

def typoglycemia(s: str) -> str:
    """
    typoglycemia is the phenomenon in which words can be read despite being jumbles.
    """
    words: str = s.split()
    for i in range(len(words)):
        word = words[i]
        if len(word) > 4:
            words[i] = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
    return ' '.join(words)

if __name__ == '__main__':
    s: str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    
    print(typoglycemia(s))