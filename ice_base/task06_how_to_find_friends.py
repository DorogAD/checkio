"""
We have an array of straight connections between drones. Each connection is represented as a string with two names of
friends separated by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should write a
function that allow determine more complex connection between drones. You are given two names also. Try to determine
if they are related through common bonds by any depth. For example: if two drones have a common friends or friends who
have common friends and so on.

Input:Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.
"""


def check_connection(network: iter, first: str, second: str) -> bool:
    for element in network:
        if first in element.split('-') and second in element.split('-'):
            return True
        if first in element.split('-'):
            cut_network = list(network)
            cut_network.remove(element)
            if first == element.split('-')[0]:
                return check_connection(cut_network, element.split('-')[1], second)
            else:
                return check_connection(cut_network, element.split('-')[0], second)
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
