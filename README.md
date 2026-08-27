# Script para la Sala de Escape
Este código fue hecho para la Sala de Escape de la Semana de la Computación 2024.
Simula ser un task manager muy simple que muestra un temporizador con cuánto tiempo le quedan a les jugadores.
Para accederlo, les jugadores necesitan ingresar el usuarix y la contraseña correspondientes.

# Ejecución
El script se corre con:
```console
python3 escaperoom.py [minutes]
```
Donde `minutes` es la cantidad de minutos inicial del temporizador. El temporizador toma valores enteros entre 1 y 99. En caso de recibir una cantidad de minutos inválida, el default son 10 minutos.

## En caso que crashee
Puede que apenas abra se crashee un poco. Encontré dos formas de resolverlo:
1. Cancelar la ejecución (`Ctrl+C`) y volver a ejecutar.
2. Cancelar la ejecución (`Ctrl+C`), limpiar la terminal (`Ctrl+L` o correr `clear`) y volver a ejecutar.

# Defaults
Por default el nombre de usuarix es `pascu`, la contraseña es `pasculindo` y el temporizador se pausa cuando se detiene la tarea llamada `Plan Malvado`.
