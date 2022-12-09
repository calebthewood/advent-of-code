
def file_to_list(path):
    """Accepts file path, converts contents to list where each line is an element"""
    file = open(path, "r")
    output = []
    for line in file:
        output.append(line.strip())
    return output

def parse_file_name(file_name):
    """
    Accepts a file name with or without extension, and returns
    just the base text of the file name
    foobar.txt >> foobar
    """
    output = ""
    for char in file_name:
        if char == ".": return output
        output += char
    return output