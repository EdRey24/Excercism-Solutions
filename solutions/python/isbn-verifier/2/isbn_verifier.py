def is_valid(isbn):
    isbn = isbn.replace("-","")
    total = 0
    if len(isbn) != 10:
        return False
    for index, char in enumerate(isbn):
        valid = "0123456789X"
        if char not in valid or (char == "X" and index != 9):
            return False
        if char == "X":
            char = "10"
        total += int(char) * (10 - index)
    return total % 11 == 0
