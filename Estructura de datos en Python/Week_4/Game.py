board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def show_board():
    for fila in board:
        print(fila)


def positions_format(position):
    fila, column = position.split(",")
    return [int(fila) - 1, int(column) - 1]


def validate_position(row, column):
    if 0 <= row <= 2 and 0 <= column <= 2:
        if board[row][column] == "-":
            return True
    return False


def validateWinner(letter):
    if board[0] == [letter, letter, letter] or\
            board[1] == [letter, letter, letter] or \
            board[2] == [letter, letter, letter]:
        return True

        # compara las columnas

    elif board[0][0] == letter and\
            board[1][0] == letter and\
            board[2][0] == letter:
        return True

    elif board[0][1] == letter and\
            board[1][1] == letter and \
            board[2][1] == letter:
        return True

    elif board[0][2] == letter and\
            board[1][2] == letter and\
            board[2][2] == letter:
        return True

        # compara las diagonales
    elif board[0][0] == letter \
            and board[1][1] == letter and\
            board[2][2] == letter:
        return True

    elif board[0][2] == letter and\
            board[1][1] == letter and\
            board[2][0] == letter:
        return True
    return False


def is_board_filled():
    for row in board:
        for item in row:
            if item == '-':
                return False
    return True


def play():
    while True:
        try:
            positions = input("Ingrese una coordenada para el tablero (fila, columna)."
                              " O digite salir para terminar el juego: ")
            if positions == "salir":
                break
            row, column = positions_format(positions)
            print(row, column)
            if validate_position(row, column):
                value = input("Digita x o o: ")
                if value == "x" or value == "o":
                    board[row][column] = value
                    show_board()
                else:
                    print("Los valores permitidos son únicamente x y o")
                result = validateWinner(value)
                if result:
                    print("Ya hay un ganador! El Jugador", value)
                    show_board()
                    break
                if is_board_filled():
                    print("Se ha presentado un empate")
                    show_board()
                    break
            else:
                print("Las coordenadas ingresadas superan el tamaño del tablero,"
                      "o para las coordenadas ingresadas ya existe valor")
        except ValueError:
            print('Op-ssss Debes enviar dos valores separados por coma')
            continue


play()
