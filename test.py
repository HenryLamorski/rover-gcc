import lib.gcchelper as gcchelper
import curses
import time
import threading
import modules.power.power as power


def get_states(state_win):
	while 1:
		state_win.box()
		state_win.addstr(1,2,"Header",curses.A_BOLD)
		
		# mission time
		zeit = time.strftime("%Y-%m-%d %H:%M:%S")
		state_win.addstr(3, 2, "Zeit:")
		state_win.addstr(3, 9, zeit)
		
		# 
		
		state_win.refresh()
		time.sleep(1)
   
def show_menu(win):
	win.clear()
	win.box()
	win.addstr(1,2,"Modules",curses.A_BOLD)
	win.addstr(3, 2, "F2:", curses.A_UNDERLINE)
	win.addstr(3, 6, "messages")
	win.addstr(4, 2, "x:", curses.A_UNDERLINE)
	win.addstr(4, 6, "Exit")
	win.refresh()

# new curses.initscr()
stdscr = gcchelper.init_curses()

# main window
y, x = stdscr.getmaxyx()
main_win = curses.newwin(y-1, x-2, 1, 1)
main_win.box()
main_win.refresh()


#######################################################################
## panels 
#######################################################################

# state_win curses.newwin(nlines, ncols, begin_y, begin_x)
l_panel = curses.newwin(10, 40, 1, 1)
# daemon
clock = threading.Thread(target=get_states, args=(l_panel,))
clock.daemon = True
clock.start()

menue_win = curses.newwin(10,40,12,1)


while True:
	# if a submodule exiting, than render menue
	show_menu(menue_win)
	c = stdscr.getch()
	if c == ord('x'):
		break
	elif c == curses.KEY_F2:
		power.show_menu(menue_win,stdscr)
	elif c == curses.KEY_F3:
		show_menu(menue_win)

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
