def is_armstrong_number(number):
    num = number
    result = 0
    digits = 0
    while num > 0:
        digits += 1
        num //= 10
    num = number
    while num > 0:
        digit = num % 10
        result += digit ** digits
        num //= 10
    return result == number
