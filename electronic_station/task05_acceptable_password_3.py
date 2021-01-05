"""
In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but cannot consist of just digits.

Input: A string.

Output: A bool.
"""


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password_2(password: str) -> bool:
    return len(password) > 6 and any([x.isdigit() for x in password])


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password_2('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password_2('short') == False
    assert is_acceptable_password_2('muchlonger') == False
    assert is_acceptable_password_2('ashort') == False
    assert is_acceptable_password_2('muchlonger5') == True
    assert is_acceptable_password_2('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password_3(password: str) -> bool:
    return len(password) > 6 and any([x.isdigit() for x in password]) and any([x.isalpha() for x in password])


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password_3('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password_3('short') == False
    assert is_acceptable_password_3('muchlonger') == False
    assert is_acceptable_password_3('ashort') == False
    assert is_acceptable_password_3('muchlonger5') == True
    assert is_acceptable_password_3('sh5') == False
    assert is_acceptable_password_3('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
