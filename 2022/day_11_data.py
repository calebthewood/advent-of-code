
def add(n1, n2):
    memory = {}
    def memoized_add(n1, n2):
        key = f"{n1}+{n2}"
        if key in memory:
            return memory[key]
        else:
            memory[key] = n1 + n2
        return memory[key]
    return memoized_add(n1, n2)


def subtract(n1, n2):
    memory = {}
    def memoized_subtract(n1, n2):
        key = f"{n1}-{n2}"
        if key in memory:
            return memory[key]
        else:
            memory[key] = n1 - n2
        return memory[key]
    return memoized_subtract(n1, n2)


def multiply(n1, n2):
    memory = {}
    def memoized_multiply(n1, n2):
        key = f"{n1}*{n2}"
        if key in memory:
            return memory[key]
        else:
            memory[key] = n1 * n2
        return memory[key]
    return memoized_multiply(n1, n2)


def divide(n1, n2):
    memory = {}
    def memoized_divide(n1, n2):
        key = f"{n1}/{n2}"
        if key in memory:
            return memory[key]
        else:
            memory[key] = n1 / n2
        return memory[key]
    return memoized_divide(n1, n2)


def square(n1, n2):
    memory = {}
    def memoized_square(n1, n2):
        key = f"{n1}**{n2}"
        if key in memory:
            return memory[key]
        else:
            memory[key] = n1 ** n2
        return memory[key]
    return memoized_square(n1, n2)


def modulo(n1, n2):
    memory = {}
    def memoized_modulo(n1, n2):
        key = f"{n1}%{n2}==0"
        if key in memory:
            return memory[key]
        else:
            memory[key] = n1 % n2 == 0
        return memory[key]
    return memoized_modulo(n1, n2)


calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square,
    "%": modulo
}


class Monkey:
    """Rascal Monkeys"""

    def __init__(self, id, items, operations, test):
        """"Create a monkey to play with your stuff."""
        self.id = id
        self.items = items
        self.operations = operations
        self.test = test
        self.inspections = 0

    def pass_item(self):
        """Decide where to pass current item"""
        worry_level = self._calculate_worry()
        test_val = self.test[0]
        monkey_a = self.test[1]
        monkey_b = self.test[2]
        modulo_func = calculator["%"]

        if modulo_func(worry_level, test_val):
            item_list = monkeys[monkey_a].items
        else:
            item_list = monkeys[monkey_b].items
        item_list.append(worry_level)

    def _calculate_worry(self):
        """How worried is the human?"""
        self._conduct_inpsection()
        item_worry = self.items.pop(0)  # base worry
        operation = self.operations[0]  # mathematical operation to do
        modifier = self.operations[1]  # differs for each monkey
        calc_func = calculator[operation]
        increased_worry = calc_func(item_worry, modifier)
        # reduced_worry = increased_worry//3
        test_divider = 23 * 19 * 13 * 17
        divider = 2 * 7 * 3 * 17 * 11 * 19 * 5 * 13
        # Divider idea comes via below link
        # https://github.com/tpatel/advent-of-code-2022/blob/main/day11.mjs#L73
        return increased_worry % divider

    def _conduct_inpsection(self):
        self.inspections += 1

    def __repr__(self):
        """Return description of area."""
        # items_held = ", ".join([str(item) for item in self.items]) or "Nothing"
        return f"<Monkey #{self.id}. Holding {len(self.items)} items. Inspections: {self.inspections}>"


monkey_data = [
    {
        "monkey": 0,
        "items": list([80]),
        "operation": ["*", 5],
        "test": [2, 4, 3],
    },
    {
        "monkey": 1,
        "items": list([75, 83, 74]),
        "operation": ["+", 7],
        "test": [7, 5, 6],
    },
    {
        "monkey": 2,
        "items": [86, 67, 61, 96, 52, 63, 73],
        "operation": ["+", 5],
        "test": [3, 7, 0]
    },
    {
        "monkey": 3,
        "items": [85, 83, 55, 85, 57, 70, 85, 52],
        "operation": ["+", 8],
        "test": [17, 1, 5],
    },
    {
        "monkey": 4,
        "items": [67, 75, 91, 72, 89],
        "operation": ["+", 4],
        "test": [11, 3, 1],
    },
    {
        "monkey": 5,
        "items": [66, 64, 68, 92, 68, 77],
        "operation": ["*", 2],
        "test": [19, 6, 2],
    },
    {
        "monkey": 6,
        "items": [97, 94, 79, 88],
        "operation": ["**", 2],
        "test": [5, 2, 7],
    },
    {
        "monkey": 7,
        "items": [77, 85],
        "operation": ["+", 6],
        "test": [13, 4, 0],
    }
]

test_data = [
    {
        "monkey": 0,
        "items": [79, 98],
        "operation": ["*", 19],
        "test": [23, 2, 3],
    },
    {
        "monkey": 1,
        "items": [54, 65, 75, 74],
        "operation": ["+", 6],
        "test": [19, 2, 0],
    },
    {
        "monkey": 2,
        "items": [79, 60, 97],
        "operation": ["**", 2],
        "test": [13, 1, 3],
    },
    {
        "monkey": 3,
        "items": [74],
        "operation": ["+", 3],
        "test": [17, 0, 1],
    }
]


def create_monkey_list(monkey_list):
    output = []
    for monkey in monkey_list:
        id = monkey["monkey"]
        items = monkey["items"]
        operations = monkey["operation"]
        test = monkey["test"]
        new_monkey = Monkey(id, items, operations, test)
        output.append(new_monkey)
    return output


monkeys = create_monkey_list(monkey_data)
