import curses
import time
import threading

def get_states(state_win):
	while 1:
		state_win.box()
		state_win.addstr(1,1,"Header",curses.A_BOLD)
		
		# mission time
		zeit = time.strftime("%Y-%m-%d %H:%M:%S")
		state_win.addstr(2, 1, "Zeit:")
		state_win.addstr(2, 8, zeit)
		
		# 
		
		state_win.refresh()
		time.sleep(1)

def init_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.refresh()
    return stdscr
    
def show_menu(win):
	win.clear()
	win.addstr(1, 0, "F2:", curses.A_UNDERLINE)
	win.addstr(1, 4, "messages")
	win.addstr(1, 13, "x:", curses.A_UNDERLINE)
	win.addstr(1, 17, "Exit")
	win.refresh()

def makla(menu_win):
	menu_win.clear()
	menu_win.addstr(1,2, "x:", curses.A_UNDERLINE)
	menu_win.addstr(1,5, "Ende ->")

	menu_win.refresh()
	
	new_win = curses.newwin(22,90,4,0)
	new_win.box()
	
	while True:
		c = stdscr.getch()
		if c == ord('x'):
			break
		elif c == ord('e'):
			new_win.addstr(5,2, "bla")
			new_win.refresh()
		elif c == ord ('f'):
			new_win.addstr(5,2, "123")
			new_win.refresh()


# new curses.initscr()
stdscr = init_curses()

state_win = curses.newwin(5, 40, 0, 0)

# menue window
menue_win = curses.newwin(0, 40, 5, 0)

# daemon
clock = threading.Thread(target=get_states, args=(state_win,))
clock.daemon = True
clock.start()

while True:
	#menue_win.clear()
	#menue_win.refresh()
	show_menu(menue_win)
	c = stdscr.getch()
	if c == ord('x'):
		break
	elif c == curses.KEY_F2:
		makla(menue_win)
		show_menu(menue_win)
	elif c == curses.KEY_F3:
		show_menu(menue_win)

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
