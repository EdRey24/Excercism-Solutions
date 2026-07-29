def rotate(text, key):
    cipher = ""
    for char in text:
        upper = False
        if char.isupper():
            upper = True
        if not char.isalpha():
            cipher += char
            continue
        new = shift(char, key, upper)
        cipher += chr(new)
    return cipher

def shift(char, key, isUpper):
    if isUpper:
        new = ord(char) + key
        if new > ord('Z'):
            diff = new - 26
            return diff
        else:
            return new
    else:
        new = ord(char) + key
        if new > ord('z'):
            diff = new - 26
            return diff
        else:
            return new
