"""
You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one
whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given
in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.
"""
import re
VOWELS = "aeiouy"


def translate(phrase: str) -> str:
    phrase = re.sub("([bcdfghjklmnpqrstvwxz]).", "\\1", phrase)
    return re.sub("([aeiouy]){3}", "\\1", phrase)


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
