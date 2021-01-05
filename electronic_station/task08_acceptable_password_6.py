"""
In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    should contain 3 different letters (or digits) even if it is longer than 10

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


def is_acceptable_password_4(password: str) -> bool:
    return (9 > len(password) > 6 and any([x.isdigit() for x in password]) and any([x.isalpha() for x in password]))\
           or (len(password) > 9)


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password_4('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password_4('short') == False
    assert is_acceptable_password_4('short54') == True
    assert is_acceptable_password_4('muchlonger') == True
    assert is_acceptable_password_4('ashort') == False
    assert is_acceptable_password_4('muchlonger5') == True
    assert is_acceptable_password_4('sh5') == False
    assert is_acceptable_password_4('1234567') == False
    assert is_acceptable_password_4('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password_5(a):
    return (9 > len(a) > 6 and any([x.isdigit() for x in a]) and any([x.isalpha() for x in a])) \
           or (len(a) > 9) and 'password' not in a.lower()


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password_5('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password_5('short') == False
    assert is_acceptable_password_5('short54') == True
    assert is_acceptable_password_5('muchlonger') == True
    assert is_acceptable_password_5('ashort') == False
    assert is_acceptable_password_5('muchlonger5') == True
    assert is_acceptable_password_5('sh5') == False
    assert is_acceptable_password_5('1234567') == False
    assert is_acceptable_password_5('12345678910') == True
    assert is_acceptable_password_5('password12345') == False
    assert is_acceptable_password_5('PASSWORD12345') == False
    assert is_acceptable_password_5('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password_6(a):
    return (9 >= len(a) > 6 and any([x.isdigit() for x in a]) and len(set(a)) >= 3 and any([x.isalpha() for x in a])) \
           or (len(a) > 9 and 'password' not in a.lower() and len(set(a)) >= 3)


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password_6('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password_6('short') == False
    assert is_acceptable_password_6('short54') == True
    assert is_acceptable_password_6('muchlonger') == True
    assert is_acceptable_password_6('ashort') == False
    assert is_acceptable_password_6('muchlonger5') == True
    assert is_acceptable_password_6('sh5') == False
    assert is_acceptable_password_6('1234567') == False
    assert is_acceptable_password_6('12345678910') == True
    assert is_acceptable_password_6('password12345') == False
    assert is_acceptable_password_6('PASSWORD12345') == False
    assert is_acceptable_password_6('pass1234word') == True
    assert is_acceptable_password_6('aaaaaa1') == False
    assert is_acceptable_password_6('aaaaaabbbbb') == False
    assert is_acceptable_password_6('aaaaaabb1') == True
    assert is_acceptable_password_6('abc1') == False
    assert is_acceptable_password_6('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
