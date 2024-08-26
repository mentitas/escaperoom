import curses
import time

def clear_line(win, y):
        height, width = win.getmaxyx()
        win.addstr(y, 1, " " * (width-2))

def get_input(win, y, x, text):
    clear_line(win, y)
    win.addstr(y, x, text)
    input = win.getstr(y, x+len(text), 20).decode('utf-8')
    return input

def login_window(win):

    correct_username = "pascu"
    correct_password = "pasculindo"

    height, width = win.getmaxyx()

    # Genero un par de colores rojo para los errores
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)

    curses.echo()
    
    win.border()
    win.addstr(0, 2, "Inicio de sesión", curses.A_STANDOUT)

    # Consigo usuario
    username = get_input(win, 2, 2, "Ingrese su nombre de usuarix: ")

    while username != correct_username:
        
        # Printeo mensaje de usuarix incorrecto
        win.addstr(2, width-4, "X", curses.color_pair(1))
        win.refresh()
        time.sleep(0.5)

        # Recibo nuevo username
        username = get_input(win, 2, 2, "Ingrese su nombre de usuarix: ")

    # Consigo contraseña
    password = get_input(win, 4, 2, "Ingrese su contraseña: ")

    while password != correct_password:
        
        # Imprimo mensaje de password incorrecta
        win.addstr(4, width-4, "X", curses.color_pair(1))
        win.refresh()
        time.sleep(0.5)

        # Recibo nueva password
        password = get_input(win, 4, 2, "Ingrese su contraseña: ")

    win.refresh()