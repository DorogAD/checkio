"""
Nikola likes to categorize everything in sight. One time Stephan gave him a label maker for his birthday, and the robots
were peeling labels off of every surface in the ship for weeks. He has since categorized all the reagents in his
laboratory, books in the library and notes on the desk. But then he learned about python dictionaries, and categorized
all the possible configurations for Sophia’s drones. Now the files are organized in a deep nested structure, but Sophia
doesn’t like this. Let's help Sophia to flatten these dictionaries.

Python dictionaries are a convenient data type to store and process configurations. They allow you to store data by keys
to create nested structures. You are given a dictionary where the keys are strings and the values are strings or
dictionaries. The goal is flatten the dictionary, but save the structures in the keys. The result should be the a
dictionary without the nested dictionaries. The keys should contain paths that contain the parent keys from the original
dictionary. The keys in the path are separated by a "/". If a value is an empty dictionary, then it should be replaced
by an empty string ("").

Let's look at an example:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

The result will be:

{"name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"}

Input: An original dictionary as a dict.

Output: The flattened dictionary as a dict.
"""


def flatten(dictionary):
    result = {}
    for key, value in dictionary.items():
        if not value:
            result[key] = ""
        elif isinstance(value, str):
            result[key] = value
        else:
            for sub_key, sub_value in flatten(value).items():
                new_key = key + "/" + sub_key
                result[new_key] = sub_value
    return result


print(flatten({"name": {"first": "Second", "last": "Drone", "nick": {}},
               "job": {"1": "scout", "2": "worker", "3": "writer", "4": "reader", "5": "learner"},
               "recent": {"places": {"earth": {"Louvre": "2015", "NY": "2017", "NP": ""}},
                          "times": {"XX": {"1964": "Yes"}, "XXI": {"2064": "Nope"}}}}))

if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    assert flatten({"name": {"first": "Second", "last": "Drone", "nick": {}},
                    "job": {"1": "scout", "2": "worker", "3": "writer", "4": "reader", "5": "learner"},
                    "recent": {"places": {"earth": {"Louvre": "2015", "NY": "2017", "NP": ""}},
                               "times": {"XX": {"1964": "Yes"}, "XXI": {"2064": "Nope"}}}}
                   ) == {"job/1": "scout", "recent/places/earth/NY": "2017", "job/3": "writer", "job/2": "worker",
                         "job/5": "learner", "job/4": "reader", "recent/places/earth/NP": "",
                         "recent/places/earth/Louvre": "2015", "recent/times/XX/1964": "Yes",
                         "recent/times/XXI/2064": "Nope", "name/first": "Second", "name/last": "Drone", "name/nick": ""}
    print('You all set. Click "Check" now!')
