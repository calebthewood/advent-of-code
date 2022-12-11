from utils import file_to_list

# Day 10: Cathode-Ray Tube

def parse_data(data):
    output = []
    for line in data:
        if line == "noop":
            output.append([line])
        else:
            [cmd, num] = line.split(" ")
            output.append(cmd)
            output.append(int(num))
    return output

def run_instructions(instructions):
    x = 1
    cycle = 1
    signal_sum = 0
    for val in instructions:
        if cycle in [20, 60, 100, 140, 180, 220]:
            strength = x * cycle
            signal_sum += strength
            print("Signal Strenght: ",strength)
        cycle += 1
        if isinstance(val, int):
            x += val
    return signal_sum

def run_program():
    input_list = file_to_list("day_10_data.txt")
    program_instructions = parse_data(input_list)
    return run_instructions(program_instructions)

print(run_program())
