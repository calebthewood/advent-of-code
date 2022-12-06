# Open the file and read its contents
def part_one(text):
    end = len(text)
    i = 3
    while i < end:
        a = text[i]
        b = text[(i - 1)]
        c = text[(i - 2)]
        d = text[(i - 3)]
        #increment before check b/c answer is 1 based count, not 0 based count
        i += 1

        if a not in [b,c,d]:
            if b not in [a,c,d]:
                if c not in [a,b,d]:
                    if d not in [a,b,c]:
                        return(i)

def part_two(text):
    window = [text[i] for i in range(0,14)]
    end = int(len(text))
    for i in range(14, end):
        if len(window) == len(set(window)): return i
        window.insert(0,text[i])
        window.pop()
    return "not found"


with open("day_6_data.txt", "r") as f:
    text = f.readline()
    print(text)
    print("len: ",len(text))
    # print("part 1 answer: ", part_one(text))
    print("part 2 answer: ", part_two(text))