def is_isogram(phrase):
    letters = set()
    phrase = phrase.lower()
    for char in phrase:
        if char in letters and (char != '-' and char != ' '):
            return False
        letters.add(char)
    return True
