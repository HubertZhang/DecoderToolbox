def print_grids(s=""):
    for i in range(2, int(len(s) / 2) + 1):
        if len(s) % i == 0:
            for j in range(int(len(s) / i)):
                print(s[j * i:(j + 1) * i])
            print('-' * 10)


def generate_grid(s="", width=2):
    r = [s[j * width:(j + 1) * width] for j in range(int(len(s) / width))]
    return r


def read_all_grid(s, func=print):
    for i in range(2, int(len(s) / 2) + 1):
        if len(s) % i == 0:
            read_all_direction(s, i, func)
            print('-' * 20)


def read_all_direction(s, width, func=print):
    t = generate_grid(s, width=width)
    for x in t:
        print(''.join(x))
    print("R:")
    for start in ["ul", "ur", "bl", "br"]:
        for direction in ["x", "y"]:
            func(read_grid(t, start=start, direction=direction))


def read_string_grid(s="", width=2, start="ul", direction="x"):
    t = generate_grid(s, width=width)
    return read_grid(t, start=start, direction=direction)


def read_grid(t=[""], start="ul", direction="x"):
    width = len(t[0])
    height = len(t)
    x_axis = None
    y_axis = None
    if "u" in start:
        y_axis = range(height)
    elif "b" in start:
        y_axis = range(height)[::-1]
    if "l" in start:
        x_axis = range(width)
    elif "r" in start:
        x_axis = range(width)[::-1]
    if x_axis is None or y_axis is None:
        raise ValueError("Missing start point in start:{}" % start)
    result = ""
    if direction == "x":
        for j in y_axis:
            for i in x_axis:
                result += t[j][i]
    elif direction == "y":
        for i in x_axis:
            for j in y_axis:
                result += t[j][i]

    return result
