import curses
import time
import math
import random

# Configuration constants
FRAME_RATE = 0.09  
INITIAL_X = 10.0
INITIAL_Y = 10.0
RADIUS = 4
DIRECTION_X = 4.5
DIRECTION_Y = 0.5
GRAVITY = 0.15
FRICTION = 0.99

def draw_sphere(stdscr, x, y, radius):
    color_pairs = [1, 2, 3, 4, 5, 6]  
    color = random.choice(color_pairs)
    stdscr.attron(curses.color_pair(color))

    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            distance = math.sqrt(i**2 + j**2)
            if radius - 0.5 < distance < radius + 0.5:
                try:
                    stdscr.addch(int(y) + i, int(x) + j, 'O')
                except curses.error:
                    pass  # Ignore errors for characters out of bounds

    stdscr.attroff(curses.color_pair(color))

def update_position(x, y, direction_x, direction_y, radius, max_x, max_y):
    direction_y += GRAVITY

    # Cap the speed to prevent excessive movement
    max_speed = 5
    direction_x = max(min(direction_x, max_speed), -max_speed)
    direction_y = max(min(direction_y, max_speed), -max_speed)

    # Check for boundary collision and reverse direction
    if x + radius >= max_x:
        x = max_x - radius
        direction_x *= -1
    elif x - radius <= 0:
        x = radius
        direction_x *= -1

    if y + radius >= max_y:
        y = max_y - radius
        direction_y *= -1
        direction_y *= FRICTION  # Apply friction to slow down bounce
    elif y - radius <= 0:
        y = radius
        direction_y *= -1
        direction_y *= FRICTION

    # Update position
    x += direction_x
    y += direction_y

    return x, y, direction_x, direction_y


def setup_colors():
    # Initialize color pairs for more visual interest
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

def move_sphere(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(0)   # Refresh rate

    setup_colors()  # Initialize color pairs

    x, y = INITIAL_X, INITIAL_Y
    direction_x, direction_y = DIRECTION_X, DIRECTION_Y

    while True:
        stdscr.clear()
        draw_sphere(stdscr, x, y, RADIUS)

        key = stdscr.getch()
        if key == ord('q'):
            break  # Quit on 'q'

        max_y, max_x = stdscr.getmaxyx()
        x, y, direction_x, direction_y = update_position(x, y, direction_x, direction_y, RADIUS, max_x, max_y)

        stdscr.refresh()  # Refresh the screen
        time.sleep(FRAME_RATE)  # Control the frame rate

if __name__ == "__main__":
    curses.wrapper(move_sphere)
