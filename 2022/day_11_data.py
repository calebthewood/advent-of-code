# Must be a better way to set up the monkey tests!

def monkey_0_test(item, worry):
    if worry % 2 == 0:
        monkeys[4].items.append(item)
    else:
        monkeys[3].items.append(item)

def monkey_1_test(item, worry):
    if worry % 7 == 0:
        monkeys[5].items.append(item)
    else:
        monkeys[6].items.append(item)

def monkey_2_test(item, worry):
    if worry % 3 == 0:
        monkeys[7].items.append(item)
    else:
        monkeys[0].items.append(item)

def monkey_3_test(item, worry):
    if worry % 17 == 0:
        monkeys[1].items.append(item)
    else:
        monkeys[5].items.append(item)

def monkey_4_test(item, worry):
    if worry % 11 == 0:
        monkeys[3].items.append(item)
    else:
        monkeys[1].items.append(item)

def monkey_5_test(item, worry):
    if worry % 19 == 0:
        monkeys[6].items.append(item)
    else:
        monkeys[2].items.append(item)

def monkey_6_test(item, worry):
    if worry % 5 == 0:
        monkeys[2].items.append(item)
    else:
        monkeys[7].items.append(item)

def monkey_7_test(item, worry):
    if worry % 13 == 0:
        monkeys[4].items.append(item)
    else:
        monkeys[0].items.append(item)

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

monkeys = [
    {
        "monkey": 0,
        "items": [80],
        "operation": operation_0,
        "test": monkey_0_test,
    },
    {
        "monkey": 1,
        "items": [75, 83, 74],
        "operation": operation_1,
        "test": monkey_1_test,
    },
    {
        "monkey": 2,
        "items": [86, 67, 61, 96, 52, 63, 73],
        "operation": operation_2,
        "test": monkey_2_test
    },
    {
        "monkey": 3,
        "items": [85, 83, 55, 85, 57, 70, 85, 52],
        "operation": operation_3,
        "test": monkey_3_test,
    },
    {
        "monkey": 4,
        "items": [67, 75, 91, 72, 89],
        "operation": operation_4,
        "test": monkey_4_test,
    },
    {"monkey": 5,
     "items": [66, 64, 68, 92, 68, 77],
     "operation": operation_5,
     "test": monkey_5_test,
     },
    {
        "monkey": 6,
        "items": [97, 94, 79, 88],
        "operation": operation_6,
        "test": monkey_6_test,
    },
    {
        "monkey": 7,
        "items": [77, 85],
        "operation": operation_7,
        "test": monkey_7_test,
    }
]
