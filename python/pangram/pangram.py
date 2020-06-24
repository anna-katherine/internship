def is_pangram(sentence):
    cleaned = ''.join(ch for ch in sentence if ch.isalpha())
    cleaned = cleaned.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    x = list(cleaned)
    for i in alphabet:
        if i not in x:
            return False
    return True
