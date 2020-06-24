def is_isogram(string):
    x = string.replace(' ','').replace('-','').lower()
    return len(x) == len(set(x))
