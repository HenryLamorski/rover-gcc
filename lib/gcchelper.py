import curses

def init_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.clear()
    stdscr.refresh()
    return stdscr
