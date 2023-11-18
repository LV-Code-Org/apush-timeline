from random import choice
import re

unitSep = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
units = {}


class Style:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    underline = '\033[4m'
    reset = '\033[0m'


def initialize_style():
    style = Style()
    return style


s = initialize_style()


def parse(li):
    return [z for z in li if z]


with open('timeline.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            lines.remove(line)
    x = "".join(lines).split(unitSep)
    for index, i in enumerate(x):
        units[index + 1] = parse(i.split("\n"))
    f.close()


def format_items(arr):
    u = []
    currentYear = ""
    for v in arr:
        if re.match(r"\d{4}:", v):
            currentYear = v.split(":")[0]
            u.append((currentYear, v.split(":")[1].strip()))
        else:
            u.append((currentYear, v))

    return u


unit = int(input("Enter unit: "))
while True:
    c = choice(format_items(units[unit]))
    x = input(s.yellow + c[1] + "\n")
    if x == c[0]:
        print(s.green + "Correct!")
    else:
        print(s.red + "Incorrect - the answer was " + s.green + c[0])
