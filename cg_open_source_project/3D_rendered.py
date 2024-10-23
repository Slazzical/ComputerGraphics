import curses
import time
import math

# Configuration constants
FRAME_RATE = 0.05
INITIAL_X = 10.0
INITIAL_Y = 10.0
RADIUS = 2  # Reduced radius
DIRECTION_X = 1.0
DIRECTION_Y = 1.0

def draw_sphere(stdscr, x, y, radius):
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            distance = math.sqrt(i**2 + j**2)
            if radius - 0.5 < distance < radius + 0.5:
                try:
                    stdscr.addch(int(y) + i, int(x) + j, 'O')
                except curses.error:
                    pass

def update_position(x, y, direction_x, direction_y, radius, max_x, max_y):
    if x + radius >= max_x or x - radius <= 0:
        direction_x *= -1
    if y + radius >= max_y or y - radius <= 0:
        direction_y *= -1

    x += direction_x
    y += direction_y

    return x, y, direction_x, direction_y

def move_sphere(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(0)

    x, y = INITIAL_X, INITIAL_Y
    direction_x, direction_y = DIRECTION_X, DIRECTION_Y

    while True:
        stdscr.clear()
        draw_sphere(stdscr, x, y, RADIUS)

        key = stdscr.getch()
        if key == ord('q'):
            break

        max_y, max_x = stdscr.getmaxyx()
        x, y, direction_x, direction_y = update_position(x, y, direction_x, direction_y, RADIUS, max_x, max_y)

        stdscr.refresh()
        time.sleep(FRAME_RATE)

if __name__ == "__main__":
    curses.wrapper(move_sphere)