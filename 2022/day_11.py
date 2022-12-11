from day_11_data import monkeys
import math


# Day 11: Monkey in the Middle

def run_round():
    for monkey in monkeys:
        operation = monkey["operation"] # function
        test = monkey["test"] # function
        num = monkey["monkey"]
        print("Monkey: ", monkey["items"])
        while len(monkey["items"]) > 0:
            # item = monkey["items"].pop(0)
            # worry = operation(item)
            # worry = math.floor(worry/3)
            # test(item, worry)
            print("Monkey #",num)

run_round()