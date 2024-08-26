import curses
import threading
import sys
from clock_window import clock_window
from login_window import login_window
from app_window   import app_window

# El tiempo del countdown está determinado por el primer parámetro de entrada de cuando se llama al script
if len(sys.argv)>1 and int(sys.argv[1]) in range(1,100):
    minutes = int(sys.argv[1])
else:
    minutes = 10

def main_window(login_win, app_win, stop_clock):
    login_window(login_win)
    app_window(app_win, stop_clock)

def main(stdscr):

    curses.curs_set(0)

    height, width = stdscr.getmaxyx()

    clock_win = curses.newwin(       12,      58,         2,  (width-58)//2)
    login_win = curses.newwin(        7,      58,        16,  (width-58)//2)
    app_win   = curses.newwin(height-16,   width,        16,              0)

    stop_clock = threading.Event()

    clock = threading.Thread(target=clock_window, args=(clock_win, minutes, stop_clock))
    main  = threading.Thread(target=main_window,  args=(login_win, app_win, stop_clock))

    clock.daemon = True
    main.daemon = True

    clock.start()
    main.start()

    clock.join()
    main.join()

if __name__ == "__main__":
    curses.wrapper(main)