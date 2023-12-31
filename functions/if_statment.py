def are_equal(num_a: int, num_b: int) -> str:
    if num_a == num_b:
        return "equal"
    else:
        return "not equal"

def positive_or_negative(num_a: int) -> str:
    if num_a > 0:
        return "positive"
    elif num_a < 0:
        return "negative"
    else:
        return "zero"

def is_in_string(letter: str, word: str) -> bool:
    return letter in word

def are_same_length(str_a: str, str_b: str) -> bool:
    return len(str_a) == len(str_b)

def is_letter_or_digit(symbol: str) -> str:
    if symbol.isalpha():
        return "letter"
    elif symbol.isdigit():
        return "digit"
    else:
        return "other"

def are_last_symbols_same(str_a: str, str_b: str) -> bool:
    if len(str_a) > 0 and len(str_b) > 0:
        return str_a[-1] == str_b[-1]
    else:
        return False

def hundred(num_a: int) -> int:
    if num_a <= 100:
        return 100 - num_a
    else:
        return num_a % 100

# Testing the functions
print(are_equal(12, 13))  # "not equal"
print(are_equal(5, 5))    # "equal"

print(positive_or_negative(12))  # "positive"
print(positive_or_negative(0))   # "zero"
print(positive_or_negative(-12))  # "negative"

print(is_in_string("a", "car"))  # True
print(is_in_string("b", "car"))  # False

print(are_same_length("aa", "bb"))  # True
print(are_same_length("a", "bbb"))   # False

print(is_letter_or_digit("a"))  # "letter"
print(is_letter_or_digit("1"))  # "digit"
print(is_letter_or_digit("?"))  # "other"

print(are_last_symbols_same("car", "house"))  # False
print(are_last_symbols_same("bird", "card"))  # True

print(hundred(45))   # 55
print(hundred(100))  # 0
print(hundred(110))  # 10