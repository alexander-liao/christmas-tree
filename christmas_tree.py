import sys, os, random, time

def draw_char(r, c, char):
    sys.stdout.write("\033[%d;%dH%s\033[1B" % (r, c, char ))

def write_char(char):
    sys.stdout.write(char)

def clear():
    ROWS, COLS = size()
    sys.stdout.write("\033[1;1H" + "\n".join(" " * COLS for _ in range(ROWS)) + "\033[1;1H")

def reset():
    sys.stdout.write("\033[0m\033[40m")

def rows():
    return os.get_terminal_size().lines

def cols():
    return os.get_terminal_size().columns

def size():
    size = os.get_terminal_size()
    return (size.lines, size.columns)

def progress_snow(snow, grid):
    snow[:] = [(particle[0] + 1, particle[1]) for particle in snow]
    ROWS, COLS = size()
    r = list(range(COLS))
    random.shuffle(r)
    for i in r[-COLS // 40:]:
        snow.append((1, i + 1))
    snow[:] = [particle for particle in snow if 0 < particle[0] <= ROWS and 0 < particle[1] <= COLS]
    for particle in snow:
        grid[particle[0] - 1][particle[1] - 1] = "\033[1;37m*\033[0m"

def draw_tree(grid):
    ROWS, COLS = size()
    if COLS % 2 == 0:
        grid[-1][COLS // 2] = "|"
    else:
        pass

snow = []
while True:
    clear()
    grid = [[' '] * cols() for _ in range(rows())]
    progress_snow(snow, grid)
    draw_tree(grid)
    sys.stdout.write("\n".join(map("".join, grid)))
    sys.stdout.flush()
    time.sleep(1)
