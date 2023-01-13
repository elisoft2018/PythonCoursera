"""
# El tablero se puede represntar como una lista, como una matriz o un diccionario.
tablero = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def dibujar_tablero(tablero):
    Dibuja el tablero en pantalla.

    print("")
    for row in tablero:
        print("|", row[0], "|", row[1], "|", row[2], "|", sep='')
    print("")

def poner_ficha(ficha):
   Coloca la ficha en la posiciÃ³n elegida por el usuario.
        Verifica que la posiciÃ³n sea correcta y que no este ocupada.

    ficha_ok = False
    while not ficha_ok:
        print("Turno:", ficha)
        try:
            fila = int(input("Seleccione una fila (0-2):"))
            col = int(input("Seleccione una columna (0-2):"))
            if tablero[fila][col] not in ('X', 'O'):
                tablero[fila][col] = ficha
                ficha_ok = True
            else:
                print("La posiciÃ³n ya esta ocupada!")
                ficha_ok = False
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print("PosiciÃ³n incorrecta!")
            ficha_ok = False

def validar_tablero(tablero):
    Valida el tablero para ver si el juego termino
        con un ganador o termino en empate o si todavÃ­a continua.
        -1: continua
         0: empate
         1: Gano O
         2: Gano X

    resultado = -1
    # Fila completa
    regla_1 = (tablero[0][0] in ('X', 'O')) and (tablero[0][0] == tablero[0][1] == tablero[0][2])
    regla_2 = (tablero[1][0] in ('X', 'O')) and (tablero[1][0] == tablero[1][1] == tablero[1][2])
    regla_3 = (tablero[2][0] in ('X', 'O')) and (tablero[2][0] == tablero[2][1] == tablero[2][2])
    # Columna completa
    regla_4 = (tablero[0][0] in ('X', 'O')) and (tablero[0][0] == tablero[1][0] == tablero[2][0])
    regla_5 = (tablero[0][1] in ('X', 'O')) and (tablero[0][1] == tablero[1][1] == tablero[2][1])
    regla_6 = (tablero[0][2] in ('X', 'O')) and (tablero[0][2] == tablero[1][2] == tablero[2][2])
    # diagonales
    regla_7 = (tablero[0][0] in ('X', 'O')) and (tablero[0][0] == tablero[1][1] == tablero[2][2])
    regla_8 = (tablero[0][2] in ('X', 'O')) and (tablero[0][2] == tablero[1][1] == tablero[2][0])

    if regla_1:
        resultado = 2 if tablero[0][0] == 'X' else 1
    elif regla_2:
        resultado = 2 if tablero[1][0] == 'X' else 1
    elif regla_3:
        resultado = 2 if tablero[2][0] == 'X' else 1
    elif regla_4:
        resultado = 2 if tablero[0][0] == 'X' else 1
    elif regla_5:
        resultado = 2 if tablero[0][1] == 'X' else 1
    elif regla_6:
        resultado = 2 if tablero[0][2] == 'X' else 1
    elif regla_7:
        resultado = 2 if tablero[0][0] == 'X' else 1
    elif regla_8:
        resultado = 2 if tablero[0][2] == 'X' else 1
    else:
        empate = True
        for row in tablero:
            for col in row:
                if col not in ('X', 'O'):
                    empate = False
                    break;
        if empate:
            resultado = 0
    return resultado

print("TA-TE-TI")
termino = False
jugadas = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
dibujar_tablero(tablero)
while not termino:
    ficha = jugadas.pop()
    poner_ficha(ficha)
    dibujar_tablero(tablero)
    status = validar_tablero(tablero)
    if status == 1:
        termino = True
        print("Gano O!")
    elif status == 2:
        termino = True
        print("Gano X!")
    elif status == 0:
        termino = True
        print("La partida terino en empate!")


import os
import sys

Ta = ['|-|', '|-|', '|-|',
      '|-|', '|-|', '|-|',
      '|-|', '|-|', '|-|']

win = None


def vertab():
    print("\n")
    print('|' + Ta[0] + '|' + Ta[1] + '|' + Ta[2] + '|   |1||2||3|')
    print('|' + Ta[3] + '|' + Ta[4] + '|' + Ta[5] + '|   |4||5||6|')
    print('|' + Ta[6] + '|' + Ta[7] + '|' + Ta[8] + '|   |7||8||9|')
    print('\n')


def winner():
    global win
    win_hor()
    win_ver()
    win_dia()


def win_hor():
    global win
    if Ta[0] == Ta[1] == Ta[2] != "|-|":
        win = Ta[0]
    elif Ta[3] == Ta[4] == Ta[5] != "|-|":
        win = Ta[3]
    elif Ta[6] == Ta[7] == Ta[8] != "|-|":
        win = Ta[6]


def win_ver():
    global win
    if Ta[0] == Ta[3] == Ta[6] != "|-|":
        win = Ta[0]
    elif Ta[1] == Ta[4] == Ta[7] != "|-|":
        win = Ta[1]
    elif Ta[2] == Ta[5] == Ta[8] != "|-|":
        win = Ta[2]


def win_dia():
    global win
    if Ta[0] == Ta[4] == Ta[8] != "|-|":
        win = Ta[0]
    elif Ta[2] == Ta[4] == Ta[6] != "|-|":
        win = Ta[2]


def jugador():
    u1 = input('Usuario 1 eliga O o X: ').upper()
    if u1 == 'O':
        u2 = 'X'
        print('El usuario 1 elijio ', u1, ' por lo tanto usuario 2 es ', u2)
        print('El usuario 2 empieza')

    elif u1 == 'X':
        u2 = 'O'
        print('El usuario 1 elijio ', u1, ' por lo tanto usuario 2 es ', u2)
        print('El usuario 1 empieza')
    return [u1, u2]


def formato():
    u1, u2 = jugador()
    validacion = '|-|'
    global win
    print('INICIO DEL JUEGO!')
    vertab()
    if u1 == 'X':
        for i in range(5):
            print('Turno del usuario 1 |X|')
            val = 'X'
            play(val)
            winner()
            if win != 'X' and i < 4:
                for j in range(3):
                    print('Turno del usuario 2 |O|')
                    val = 'O'
                    play(val)
                    winner()
                    if win == 'O':
                        print('Jugador 2 ..... Ganaste!')
                        fin()
                    break
            elif win == 'X':
                print('Jugador 1 ..... Ganaste!')
                fin()
            else:
                print('Empate')
    elif u2 == 'X':
        for i in range(5):
            print('Turno del usuario 2 |X|')
            val = 'X'
            play(val)
            winner()
            if win != 'X' and i < 4:
                for j in range(3):
                    print('Turno del usuario 1 |O|')
                    val = 'O'
                    play(val)
                    winner()
                    if win == 'O':
                        print('Jugador 1 ..... Ganaste!')
                        fin()
                    break
            elif win == 'X':
                print('Jugador 2 ..... Ganaste!')
                fin()
            else:
                print('Empate')


def fin():
    print("Presione ENTER")
    os.system("pause")
    os.system('cls')
    sys.exit()


def play(val):
    an = False
    while an == False:
        pos = int(input('Elija una posición del 1 al 9: '))
        pos -= 1
        if Ta[pos] == '|-|':
            an = True
        else:
            print('¡Posicion ocupa! Por favor elija otra posicion')
    Ta[pos] = val
    vertab()


def GameOn():
    print("\n")
    formato()


GameOn()



# Ta Te Ti

import random      
def dibujarTablero(tablero):

     # Esta función dibuja el tablero recibido como argumento.
     # "tablero" es una lista de 10 cadenas representando la pizarra (ignora índice 0)
     print('   |   |')
     print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
     print('   |   |')
     print('-----------')
     print('   |   |')
     print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
     print('   |   |')

def ingresaLetraJugador():
     # Permite al jugador typear que letra desea ser.
     # Devuelve una lista con las letras de los jugadores como primer item, y la de la computadora como segundo.
     letra = ''
     while not (letra == 'X' or letra == 'O'):
         print('¿CUAL QUIERES ELEGIR X o O?')
         letra = input().upper()

     # el primer elemento de la lista es la letra del jugador, el segundo es la letra de la computadora.
     if letra == 'X':
         return ['X', 'O']
     else:
         return ['O', 'X']

def quienComienza():
     # Elije al azar que jugador comienza.
     if random.randint(0, 1) == 0:
         return 'La computadora'
     else:
         return 'El jugador'

def jugarDeNuevo():
     # Esta funcion devuelve True (Verdadero) si el jugador desea volver a jugar, de lo contrario devuelve False (Falso).
     print('¿Deseas volver a jugar? (sí/no)?')
     return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
     tablero[jugada] = letra

def esGanador(ta, le):
     # Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado.
     # Utilizamos reemplazamos tablero por ta y letra por le para no escribir tanto.
     return ((ta[7] == le and ta[8] == le and ta[9] == le) or # horizontal superior
     (ta[4] == le and ta[5] == le and ta[6] == le) or # horizontal medio
     (ta[1] == le and ta[2] == le and ta[3] == le) or # horizontal inferior
     (ta[7] == le and ta[4] == le and ta[1] == le) or # vertical izquierda
     (ta[8] == le and ta[5] == le and ta[2] == le) or # vertical medio
     (ta[9] == le and ta[6] == le and ta[3] == le) or # vertical derecha
     (ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
     (ta[9] == le and ta[5] == le and ta[1] == le)) # diagonal

def obtenerDuplicadoTablero(tablero):
     # Duplica la lista del tablero y devuelve el duplicado.
     dupTablero = []

     for i in tablero:
         dupTablero.append(i)

     return dupTablero

def hayEspacioLibre(tablero, jugada):
     # Devuelte true si hay espacio para efectuar la jugada en el tablero.
     return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
     # Permite al jugador escribir su jugada.
     jugada = ' '
     while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
         print('¿Cuál es tu próxima jugada? (1-9)')
         jugada = input()
     return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
     # Devuelve una jugada válida en el tablero de la lista recibida.
     # Devuelve None si no hay ninguna jugada válida.
     jugadasPosibles = []
     for i in listaJugada:
         if hayEspacioLibre(tablero, i):
             jugadasPosibles.append(i)

     if len(jugadasPosibles) != 0:
         return random.choice(jugadasPosibles)
     else:
         return None

def obtenerJugadaComputadora(tablero, letraComputadora):
     # Dado un tablero y la letra de la computadora, determina que jugada efectuar.
     if letraComputadora == 'X':
         letraJugador = 'O'
     else:
         letraJugador = 'X'

     # Aquí está nuestro algoritmo para nuestra IA (Inteligencia Artifical) del Ta Te Ti.
     # Primero, verifica si podemos ganar en la próxima jugada
     for i in range(1, 10):
         copia = obtenerDuplicadoTablero(tablero)
         if hayEspacioLibre(copia, i):
             hacerJugada(copia, letraComputadora, i)
             if esGanador(copia, letraComputadora):
                 return i

     # Verifica si el jugador podría ganar en su próxima jugada, y lo bloquea.
     for i in range(1, 10):
         copia = obtenerDuplicadoTablero(tablero)
         if hayEspacioLibre(copia, i):
             hacerJugada(copia, letraJugador, i)
             if esGanador(copia, letraJugador):
                 return i

     # Intenta ocupar una de las esquinas de estar libre.
     jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
     if jugada != None:
         return jugada

     # De estar libre, intenta ocupar el centro.
     if hayEspacioLibre(tablero, 5):
         return 5

     # Ocupa alguno de los lados.
     return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
     # Devuelve True si cada espacio del tablero fue ocupado, caso contrario devuele False.
     for i in range(1, 10):
         if hayEspacioLibre(tablero, i):
             return False
     return True

print('¡HOLA, bienvenido al TATETI :D!')
while True:
     # Resetea el tablero
     elTablero = [' '] * 10
     letraJugador, letraComputadora = ingresaLetraJugador()
     turno = quienComienza()
     print(turno + ' irá primero.')
     juegoEnCurso = True

     while juegoEnCurso:
         if turno == 'El jugador':
             # Turno del jugador
             dibujarTablero(elTablero)
             jugada = obtenerJugadaJugador(elTablero)
             hacerJugada(elTablero, letraJugador, jugada)

             if esGanador(elTablero, letraJugador):

                 dibujarTablero(elTablero)
                 print('¡BIEN, GANASTE!')
                 juegoEnCurso = False
             else:
                 if tableroCompleto(elTablero):
                     dibujarTablero(elTablero)
                     print('¡Empateeeee!')
                     break
                 else:
                     turno = 'La computadora'

         else:
             # Turno de la computadora
             jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
             hacerJugada(elTablero, letraComputadora, jugada)

             if esGanador(elTablero, letraComputadora):
                 dibujarTablero(elTablero)
                 print('¡La computadora te gano ! PERDISTE.')
                 juegoEnCurso = False
             else:
                 if tableroCompleto(elTablero):
                     dibujarTablero(elTablero)
                     print('¡EMPATEEEEE!')
                     break
                 else:
                     turno = 'El jugador'

     if not jugarDeNuevo():
         break


"""