import curses
import time
import sys
import os


uno = r"""
    $$\   
  $$$$ |  
  \_$$ |  
    $$ |  
    $$ |  
    $$ |  
  $$$$$$\ 
  \______|
"""

dos = r"""
 $$$$$$\  
$$  __$$\ 
\__/  $$ |
 $$$$$$  |
$$  ____/ 
$$ |      
$$$$$$$$\ 
\________|
"""

tres = r"""
 $$$$$$\  
$$ ___$$\ 
\_/   $$ |
  $$$$$ / 
  \___$$\ 
$$\   $$ |
\$$$$$$  |
 \______/ 
"""

cuatro = r"""
$$\   $$\ 
$$ |  $$ |
$$ |  $$ |
$$$$$$$$ |
\_____$$ |
      $$ |
      $$ |
      \__|
"""

cinco = r"""
$$$$$$$\  
$$  ____| 
$$ |      
$$$$$$$\  
\_____$$\ 
$$\   $$ |
\$$$$$$  |
 \______/ 
"""

seis = r"""
$$$$$$\   
$$  __$$\ 
$$ /  \__|
$$$$$$$\  
$$  __$$\ 
$$ /  $$ |
 $$$$$$  |
 \______/ 
"""

siete = r"""
$$$$$$$$\ 
\____$$  |
    $$  / 
   $$  /  
  $$  /   
 $$  /    
$$  /     
\__/      
"""

ocho = r"""
 $$$$$$\  
$$  __$$\ 
$$ /  $$ |
 $$$$$$  |
$$  __$$< 
$$ /  $$ |
\$$$$$$  |
 \______/ 
"""

nueve = r"""
$$$$$$\   
$$  __$$\ 
$$ /  $$ |
\$$$$$$$ |
 \____$$ |
$$\   $$ |
\$$$$$$  |
 \______/ 
"""

cero = r"""
$$$$$$\   
$$$ __$$\ 
$$$$\ $$ |
$$\$$\$$ |
$$ \$$$$ |
$$ |\$$$ |
\$$$$$$  /
 \______/ 
"""

dos_puntitos = r"""
          
          
   $$\    
   \__|   
          
   $$\    
   \__|   
          
"""

numbers_as_str = [cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve]

def print_time(win, y, x, number_1, number_2, number_3, number_4, theme):

    # IMPORTANTE: si el ascii art del número no es del tamaño declarado acá, SE VA A ROMPER
    height = 8
    width  = 11
    
    string_1 = numbers_as_str[number_1]
    string_2 = numbers_as_str[number_2]
    string_3 = numbers_as_str[number_3]
    string_4 = numbers_as_str[number_4]

    for i in range(0, height*width,width):
        row_1 =     string_1[i+1:i+width]
        row_2 =     string_2[i+1:i+width]
        row_p = dos_puntitos[i+1:i+width]
        row_3 =     string_3[i+1:i+width]
        row_4 =     string_4[i+1:i+width]

        win.addstr(y, x, f"{row_1} {row_2} {row_p} {row_3} {row_4}", theme)
        y+=1

def clock_window(win, minutes, stop_clock):

    seconds = minutes * 60
    curses.init_pair(2, curses.COLOR_RED,   -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)

    while seconds > 0:

        # Obtengo minutos y segundos
        m, s = divmod(seconds, 60)

        # Obtengo los digitos individuales de los minutos y segundos
        m_1, m_2 = divmod(m, 10)
        s_1, s_2 = divmod(s, 10)

        win.clear()

        win.addstr(0, 2, "Tiempo restante para completar 'Plan Malvado': ")
        print_time(win, 2, 2, m_1,m_2,s_1,s_2, curses.color_pair(2))
        
        win.refresh()

        time.sleep(1)
        seconds -= 1

        if stop_clock.is_set():
            break

    print_time(win, 2, 2, m_1,m_2,s_1,s_2, curses.color_pair(3))

    # Calculo cuánto tiempo estuvo activo el temporizador
    m, s = divmod(minutes*60 - seconds - 1, 60)
    win.addstr(11, 2, f"Se detuvo la tarea luego de {m:02}:{s:02}")

    win.refresh()
    #os.system("vlc FELIZ\ CUMPLEAÑOS.mp3")