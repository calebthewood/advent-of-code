from day_11_data import monkeys

# Day 11: Monkey in the Middle
def print_list(msg, list):
    print(msg)
    for item in list: print("--> ",item)

def run_round():
    for monkey in monkeys:
        # print("Before: ",monkey)
        while len(monkey.items) > 0:
            monkey.pass_item()
        # print("After: ",monkey)

def monkey_business(monkeys):
    for round in range(1,10001):
        run_round()
        if round % 1000 == 0:
            print_list(f"Round: {round}",monkeys)

    inspections = [m.inspections for m in monkeys]
    inspections.sort()
    inspections.reverse()
    print("Inspections: ", inspections)
    print("Monkey Business: ",inspections[0] * inspections[1])

monkey_business(monkeys)
