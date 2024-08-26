import curses

def clear_line(win, y):
        height, width = win.getmaxyx()
        win.addstr(y, 1, " " * (width-2))

def get_input(win, y, x, text):
    clear_line(win, y)
    win.addstr(y, x, text)
    input = win.getstr(y, x+len(text), 20).decode('utf-8')
    return input

nombre_de_tarea_objetivo = "Plan Malvado: Bajando notas de estudiantes de la UBA"

tareas = [("Actualizando Candy Crush",                                                          4,  100),
          ("Renderizando video essay 'Hatsune Miku: ¿Cebolla de verdeo o puerro?'",            32,  100),
          (nombre_de_tarea_objetivo,                                                           95,  100),
          ("Imprimiendo 'Wikihow: Cómo hackear una base de datos en 10 simples pasos'",        30,  100),
          ("Descarga de capítulos de One Piece",                                              482, 1113),
          ]

tareas_len_inicial = len(tareas)

# Busco longitud máxima de nombre de proceso
max_len = 0
for nombre, _, _ in tareas:
    if len(nombre) > max_len:
        max_len = len(nombre)

def print_tasks(win, y, x, tareas):

    # Limpio donde estaba la tabla
    for i in range(y, y+11):
        clear_line(win, i)

    win.addstr(y, x, "Tareas actuales:")
    y+=2

    titulos = ["#", "Nombre del proceso", "Progreso"]
    ancho_1 = 1                             # Ancho de la primera columna
    ancho_2 = max(len(titulos[1]), max_len) # Ancho de segunda columna
    ancho_3 = len(titulos[2])               # Ancho de tercera columna

    # Primer linea
    win.addstr(y, x, "╔═" + "═"*ancho_1 + "═╦═" + "═"*ancho_2 + "═╦═" + "═"*ancho_3 + "═╗")
    y+=1

    win.addstr(y, x, f"║ # ║ {titulos[1]:{ancho_2}s} ║ {titulos[2]:{ancho_3}s} ║")
    y+=1

    win.addstr(y, x, "╠═" + "═"*ancho_1 + "═╬═" + "═"*ancho_2 + "═╬═" + "═"*ancho_3 + "═╣")
    y+=1
    
    for i in range(0, len(tareas)):
        nombre   = tareas[i][0]
        progreso = tareas[i][1]
        total    = tareas[i][2]
        porcentaje = str(progreso) + "/" + str(total)

        win.addstr(y, x, f"║ {i} ║ {nombre:{ancho_2}s} ║ {porcentaje:>{ancho_3}s} ║")
        y+=1

    # Última linea
    win.addstr(y, x, "╚═" + "═"*ancho_1 + "═╩═" + "═"*ancho_2 + "═╩═" + "═"*ancho_3 + "═╝")

    win.refresh()


def app_window(win, stop_clock):
    
    height, width = win.getmaxyx()

    win.border()
    win.addstr(0, 2, "Detenedor de tareas", curses.A_STANDOUT)

    while tareas:
        print_tasks(win, 2, 2, tareas)

        indice_de_tarea = get_input(win, 14, 2, "Ingrese el índice de la tarea que desee detener: ")

        # Borro "Se detuvo la tarea..."
        clear_line(win, height-2)

        if indice_de_tarea.isdigit() and int(indice_de_tarea) in range(0, len(tareas)):

            nombre_de_tarea = tareas[int(indice_de_tarea)][0]
            confirmacion = get_input(win, 15, 2, f"¿Estás segurx que desea detener la tarea '{nombre_de_tarea}'? (y/n) ")

            if confirmacion == "y" or confirmacion == "Y":

                win.addstr(height-2, 2, f"Se detuvo la tarea '{nombre_de_tarea}'")
                tareas.pop(int(indice_de_tarea))

                if nombre_de_tarea == nombre_de_tarea_objetivo:
                    # Detengo el cronómetro
                    stop_clock.set()
            
            elif confirmacion == "n" or confirmacion == "N":
                
                win.addstr(height-2, 2, f"No se detuvo ninguna tarea")

        else:

            clear_line(win, height-2)
            win.addstr(height-2, 2, "Índice de tarea inválido, intente nuevamente.")

        for i in range(14, height-2):
            clear_line(win, i)

        win.refresh()

    print_tasks(win, 2, 2, tareas)

    win.addstr(17, 2, "No hay más tareas.")
    win.refresh()