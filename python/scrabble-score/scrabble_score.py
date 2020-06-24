def score(word):
    word = word.upper()
    one = ['A','E','I','O','U','L','N','R','S','T']
    two = ['D','G']
    three = ['B','C','M','P']
    four = ['F','H','V','W','Y']
    five = ['K']
    eight = ['J','X']
    ten = ['Q','Z']
    score = 0
    for i in word:
        if i in one:
            score += 1
        if i in two:
            score += 2
        if i in three:
            score += 3
        if i in four:
            score += 4
        if i in five:
            score += 5
        if i in eight:
            score += 8
        if i in ten:
            score += 10
    return score
