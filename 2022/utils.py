
def file_to_list(path):
    """Accepts file path, converts contents to list where each line is an element"""
    file = open(path, "r")
    output = []
    for line in file:
        output.append(line.strip())
    return output
