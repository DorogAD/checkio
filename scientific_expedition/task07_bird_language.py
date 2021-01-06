"""
You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one
whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given
in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.
"""
VOWELS = "aeiouy"


def translate(phrase: str) -> str:
    for letter in VOWELS:
        phrase = phrase.replace(letter * 3, letter)
    result = ''
    for i in range(len(phrase)):
        if phrase[i] not in VOWELS:
            result += phrase[i]
        elif phrase[i - 1] in VOWELS or phrase[i - 1] == ' ':
            result += phrase[i]
    return result


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
