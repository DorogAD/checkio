"""
This is the second task on parsing YAML. It represents the next step where parsing gets more complicated. The data
types, such as null and bool, are being added, and besides that, you’re getting the ability to use quotes in strings.

Here are some of the examples:

name: "Bob Dylan"
children: 6

{
  "name": "Bob Dylan",
  "children": 6
}

As you can see, the string can be put in quotes. It can be both double and single quotes.

name: "Bob Dylan"
children: 6
alive: false

{
  "name": "Bob Dylan",
  "alive": False,
  "children": 6
}

true and false are the keywords defining the boolean type.

name: "Bob Dylan"
children: 6
coding:

{
  "coding": None,
  "name": "Bob Dylan",
  "children": 6
}

If no value is specified, it becomes undefined. There also is a keyword for this - null.

Input: A format string.

Output: An object.
"""
# Taken from mission YAML. Simple Dict
import re


def yaml(a: str) -> dict:
    result = dict([pair.split(": ") for pair in a.splitlines() if pair])
    for result_key, result_value in result.items():
        result[result_key] = int(result_value) if result_value.isdigit() else result_value
    return result


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")


def yaml_2(a: str) -> dict:
    result = {}
    for line in a.splitlines():
        try:
            key, value = line.split(':')
        except ValueError:
            continue
        if value:
            value = value.strip()
        if not value or value == 'null':
            value = None
        elif value.startswith('"') and value.endswith('"'):
            value = eval(value)
        elif value == 'false':
            value = False
        elif value == 'true':
            value = True
        else:
            try:
                value = int(value)
            except ValueError:
                pass
        result[key] = value
    return result


if __name__ == '__main__':
    print("Example:")
    print(yaml_2('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml_2('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml_2('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml_2('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml_2('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml_2('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    assert yaml_2('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml_2('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    assert yaml_2('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
