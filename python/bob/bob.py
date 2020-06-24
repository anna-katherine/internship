def response(hey_bob):
    if len(hey_bob) == 0 or hey_bob.isspace():
        return "Fine. Be that way!"
    hey_bob = hey_bob.strip()
    question = False
    yelling = hey_bob.isupper()
    if hey_bob[-1] == "?":
        question = True
    if question and yelling:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if yelling:
        return "Whoa, chill out!"
    return "Whatever."
