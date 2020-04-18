""" Conway's Game of Life """
import curses

cursor = [0, 0]  # y, x

# init screen
screen = curses.initscr()
curses.start_color()
max_y, max_x = screen.getmaxyx()

cells = [[0 for x in range(max_x)] for y in range(max_y)]


def handle_keypress(keycode):
    """ Handle keypress actions """

    if keycode == 65:  # up
        cursor[0] -= 1
    elif keycode == 66:  # down
        cursor[0] += 1
    elif keycode == 67:  # right
        cursor[1] += 1
    elif keycode == 68:  # left
        cursor[1] -= 1
    elif keycode == 120:  # x
        cells[cursor[0]][cursor[1]] = 0 if cells[cursor[0]][cursor[1]] == 1 else 1


def clip_cursor_to_window():
    """ Keep a cursor within the bounds of the window """

    if cursor[0] < 0:
        cursor[0] = 0
    elif cursor[0] >= max_y:
        cursor[0] = max_y - 1

    if cursor[1] < 0:
        cursor[1] = 0
    elif cursor[1] >= max_x:
        cursor[1] = max_x - 1


def draw():
    for y in range(0, max_y):
        for x in range(0, max_x):
            if cells[y][x] == 1:
                screen.addch(y, x, "a")


def draw_cursor():
    """ Draw the cursor on the screen """
    screen.move(cursor[0], cursor[1])


# loop
def game():

    # Handle keypress
    c = screen.getch()
    handle_keypress(c)
    clip_cursor_to_window()

    # Redraw window
    screen.clear()
    draw()
    draw_cursor()

    return True


while game():
    pass

curses.endwin()
