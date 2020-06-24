def abbreviate(words):
    words = words.upper().replace('-',' ').replace('_','').split()
    acronym = ""
    for i in words:
        acronym += i[0]
    return acronym
