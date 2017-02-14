import curses

def show_menu(menu_win,stdscr):
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
