# Must be a better way to set up the monkey tests!

def operation_0(old):
    return old * 5


def operation_1(old):
    return old + 7


def operation_2(old):
    return old + 5


def operation_3(old):
    return old + 8


def operation_4(old):
    return old + 4


def operation_5(old):
    return old * 2


def operation_6(old):
    return old * old


def operation_7(old):
    return old + 6

class Monkey:
    """Rascal Monkeys"""
    def __init__(self, id, items, operations, test):
        """"Create triangle from a and b sides."""
        self.id = id
        self.items = items
        self.operations = operations
        self.test = test

    def pass_item(self):
        """Decide where to pass current item"""
        print("Test Ran")
        item = self.items.pop(0)
        worry = _calculate_worry()
        if worry % 2 == 0:
            item_list = monkeys[monkey_a]["items"]
        else:
            item_list = monkeys[monkey_b]["items"]
        item_list.append(item)

    def _calculate_worry(self, worry, operation):
        """How worried is the human?"""

        return worry

    def describe(self):
        """Return description of area."""
        return f"My area is {self.get_area()}"

monkeys = [
    {
        "monkey": 0,
        "items": [80],
        "operations": ["*",5],
        "test": [7,5,6],
    },
    {
        "monkey": 1,
        "items": [75, 83, 74],
        "operation": ["+",7],
        "test": [7,5,6],
    },
    {
        "monkey": 2,
        "items": [86, 67, 61, 96, 52, 63, 73],
        "operation": ["+", 5],
        "test": [3,7,0]
    },
    {
        "monkey": 3,
        "items": [85, 83, 55, 85, 57, 70, 85, 52],
        "operation": ["+",8],
        "test": [17,1,5],
    },
    {
        "monkey": 4,
        "items": [67, 75, 91, 72, 89],
        "operation": ["+",4],
        "test": [11,3,1],
    },
    {
        "monkey": 5,
        "items": [66, 64, 68, 92, 68, 77],
        "operation": ["*",2],
        "test": [19,6,2],
    },
    {
        "monkey": 6,
        "items": [97, 94, 79, 88],
        "operation": ["**",2],
        "test": [5,2,7],
    },
    {
        "monkey": 7,
        "items": [77, 85],
        "operation": ["+",6],
        "test": [13,4,0],
    }
]
