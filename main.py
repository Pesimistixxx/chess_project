import copy
board = [["r","n","b","q","k","b","n","r"],["p","p","p","p","p","p","p","p"],["Q",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],["P","P","P","P","P","P","P","P"],["R","N","B","Q","K","B","N","R"]]
#board = [["r","n","b","q","k","b","n","r"],["p","p","p","p","p","p","p","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".","Q",".",".",".",".","."],[".",".",".",".",".",".",".","."],["P","P","P","P","P","P","P","P"],["R","N","B","Q","K","B","N","R"]]
#board = [[".","K",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],["Q",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],["k","Q",".",".",".",".",".","."]]
def print_board():
    print("  A B C D E F G H  ")
    for i,row in enumerate(board):
        print(8-i, *row, 8 - i)
    print("  A B C D E F G H  ")

def is_valid_move(y, x, color):
    if 0 <= x < 8 and 0 <= y < 8:
        target = board[y][x]
        if target == ".":
            return True
        elif (target.islower() and color == "BLACK") or (target.isupper() and color == "WHITE"):
            return False
        else:
            return True
    return False

def pawn_moves(px, py, color):
    pmoves = []
    if color == "WHITE":
        if (px + 1) <= 7 and board[py - 1][px + 1] != "." and board[py - 1][px + 1].islower():
            pmoves.append([px + 1, py - 1])
        if (px - 1) >= 0 and board[py - 1][px - 1] != "." and board[py - 1][px - 1].islower():
            pmoves.append([px - 1, py - 1])
        if py == 6 and board[py - 2][px] == "." and board[py - 1][px] == ".":
            pmoves.append([px,py - 2])
        if (py - 1) >= 0 and board[py - 1][px] == ".":
            pmoves.append([px, py - 1])
    if color == "BLACK":
        if (px + 1) <= 7 and board[py + 1][px + 1] != "." and board[py + 1][px + 1].isupper():
            pmoves.append([px + 1, py + 1])
        if (px - 1) >= 0 and board[py + 1][px - 1] != "." and board[py + 1][px - 1].isupper():
            pmoves.append([px - 1, py + 1])
        if py == 1 and board[py + 2][px] == "." and board[py + 1][px] == ".":
            pmoves.append([px, py + 2])
        if (py + 1) <= 7 and board[py+ 1][px] == ".":
            pmoves.append([px, py + 1])
    return pmoves


def rook_moves(rx, ry, color):
    rmoves = []
    crx = rx
    while crx >= 1:
        crx -= 1
        if board[ry][crx] != "." and ((board[ry][crx].islower() and color == "BLACK") or(board[ry][crx].isupper() and color == "WHITE")):
            pass
        else:
            rmoves.append([crx, ry])
        if board[ry][crx] != ".":
            break
    crx = rx
    while crx <= 6:
        crx += 1
        if board[ry][crx] != "." and (
                (board[ry][crx].islower() and color == "BLACK") or (board[ry][crx].isupper() and color == "WHITE")):
            pass
        else:
            rmoves.append([crx, ry])
        if board[ry][crx] != ".":
            break
    cry = ry
    while cry >= 1:
        cry -= 1
        if board[cry][rx] != "." and ((board[cry][rx].islower() and color == "BLACK") or (board[cry][rx].isupper() and color == "WHITE")):
            pass
        else:
            rmoves.append([rx, cry])
        if board[cry][rx] != ".":
            break
    cry = ry
    while cry <= 6:
        cry += 1
        if board[cry][rx] != "." and (
                (board[cry][rx].islower() and color == "BLACK") or (board[cry][rx].isupper() and color == "WHITE")):
            pass
        else:
            rmoves.append([rx, cry])
        if board[ry][crx] != ".":
            break
    return rmoves

def bishop_moves(bx, by, color):
    bmoves = []
    cbx = bx
    cby = by
    while cbx >= 1 and cby >= 1:
        cbx -= 1
        cby -= 1
        if board[cby][cbx] != "." and (
                (board[cby][cbx].islower() and color == "BLACK") or (board[cby][cbx].isupper() and color == "WHITE")):
            pass
        else:
            bmoves.append([cbx, cby])
        if board[cby][cbx] != ".":
            break
    cbx = bx
    cby = by
    while cbx <= 6 and cby >= 1:
        cbx += 1
        cby -= 1
        if board[cby][cbx] != "." and (
                (board[cby][cbx].islower() and color == "BLACK") or (board[cby][cbx].isupper() and color == "WHITE")):
            pass
        else:
            bmoves.append([cbx, cby])
        if board[cby][cbx] != ".":
            break
    cby = by
    cbx = bx
    while cbx >= 1 and cby <= 6:
        cby += 1
        cbx -= 1
        if board[cby][cbx] != "." and (
                (board[cby][cbx].islower() and color == "BLACK") or (board[cby][cbx].isupper() and color == "WHITE")):
            pass
        else:
            bmoves.append([cbx, cby])
        if board[cby][cbx] != ".":
            break
    cby = by
    cbx = bx
    while cbx <= 6 and cby <= 6:
        cby += 1
        cbx += 1
        if board[cby][cbx] != "." and (
                (board[cby][cbx].islower() and color == "BLACK") or (board[cby][cbx].isupper() and color == "WHITE")):
            pass
        else:
            bmoves.append([cbx, cby])
        if board[cby][cbx] != ".":
            break
    return bmoves


def king_moves(kx, ky, color):
    kmoves = []
    possible_moves = [[kx + 1, ky + 1],[kx + 1, ky],[kx, ky + 1],[kx + 1, ky - 1], [kx, ky - 1], [kx - 1, ky - 1], [kx - 1, ky + 1],[kx - 1, ky]]
    for x, y in possible_moves:
        if is_valid_move(y,x,color):
            kmoves.append([x,y])
    return kmoves


def queen_moves(qx, qy, color):
    return bishop_moves(qx, qy, color) + rook_moves(qx, qy, color)


def knight_moves(kx, ky, color):
    kmoves = []
    possible_moves = [[kx + 2, ky + 1],[kx + 1, ky + 2],[kx - 1, ky + 2],[kx - 2, ky + 1],[kx - 2, ky - 1],[kx - 1, ky - 2],[kx + 1, ky - 2],[kx + 2, ky - 1]]
    for x,y in possible_moves:
        if is_valid_move(y,x,color):
            kmoves.append([x,y])
    return kmoves

def translate_cords(fx, fy):
    if not validate_coords(fx, fy):
        return -1, -1
    return letters_to_column[fx], 8 - fy


def detranslate_cords(fx, fy):
    return column_to_letters[fx], 8 - fy

def check_moves(fx, fy, boar = board):
    color = None
    figure = boar[fy][fx]
    if figure == ".":
        print("На этой клетке нет фигуры")
        return "Error"
    if figure.islower():
        color = "BLACK"
    if figure.isupper():
        color = "WHITE"
    figure = figure.lower()
    if figure == "p":
        moves = pawn_moves(fx, fy, color)
    elif figure == "r":
        moves = rook_moves(fx, fy, color)
    elif figure == "b":
        moves = bishop_moves(fx, fy, color)
    elif figure == "q":
        moves = queen_moves(fx, fy, color)
    elif figure == "k":
        moves = king_moves(fx, fy, color)
    elif figure == "n":
        moves = knight_moves(fx, fy, color)
    else:
        print("Ошибка")
        return "Error"
    return moves


def is_checkmate(color):
    pbking_cords = []
    pwking_cords = []
    w_moves = []
    b_moves = []
    bk_cords = []
    wk_cords = []
    bk_moves = []
    wk_moves = []
    for i in range(8):
        for j in range(8):
            i, j = translate_cords(i, j)
            if board[i][j] == "K":
                wk_cords = [i,j]
                for mov in check_moves(i,j):
                    wk_moves.append(mov)
            elif board[i][j] == "k":
                bk_cords = [i,j]
                for mov in check_moves(i,j):
                    bk_moves.append(mov)
            elif board[i][j].isupper():
                for mov in check_moves(i,j):
                    w_moves.append(mov)
            elif board[i][j].islower():
                for mov in check_moves(i,j):
                    b_moves.append(mov)
    if color == "BLACK":
        for i in range(8):
            for j in range(8):
                if board[i][j].islower():
                    for mov in check_moves(j,i):
                        p_moves = []
                        board_tmp = copy.deepcopy(board)
                        board_tmp[mov[1]][mov[0]] = board_tmp[i][j]
                        board_tmp[i][j] = "."
                        for k in range(8):
                            for l in range(8):
                                if board_tmp[k][l].isupper():
                                    for movv in check_moves(l,k,board_tmp):
                                        p_moves.append(movv)
                                if board_tmp[k][l] == "k":
                                    pbking_cords = [l,k]
                        if pbking_cords not in p_moves:
                            return False
        return True
    if color == "WHITE":
        for i in range(8):
            for j in range(8):
                if board[i][j].isupper():
                    for mov in check_moves(j,i):
                        p_moves = []
                        board_tmp = copy.deepcopy(board)
                        board_tmp[mov[1]][mov[0]] = board_tmp[i][j]
                        board_tmp[i][j] = "."
                        for k in range(8):
                            for l in range(8):
                                if board_tmp[k][l].islower():
                                    for movv in check_moves(l,k,board_tmp):
                                        p_moves.append(movv)
                                if board_tmp[k][l] == "K":
                                    pwking_cords = [l,k]
                        if pwking_cords not in p_moves:
                            return False
        return True
def validate_coords(fx, fy):
    if fx in letters_to_column and 8 >= fy >= 1:
        return True
    return False
letters_to_column = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7}
column_to_letters = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H"}


def main():
    global board
    bshah = False
    wshah = False
    game_process = True
    turn_cnt = 1
    turn = "WHITE"
    history_of_game = []
    print_board()

    while game_process:
        b_moves = []
        w_moves = []
        bking_coords = []
        wking_coords = []

        for i in range(8):
            for j in range(8):
                if board[i][j].islower():
                    for move in check_moves(j,i):
                        b_moves.append(move)
                if board[i][j].isupper():
                    for move in check_moves(j, i):
                        w_moves.append(move)
                if board[i][j] == "k":
                    bking_coords = [j,i]
                if board[i][j] == "K":
                    wking_coords = [j,i]
        if bking_coords in w_moves:
            bshah = True
            if is_checkmate("BLACK"):
                print("Шах и мат, победили белые")
                break
            print("ВНИМАНИЕ, Шах чёрному королю")
        if wking_coords in b_moves:
            wshah = True
            if is_checkmate("WHITE"):
                print("Шах и мат победили черные")
                break
            print("Внимание, шах белому королю")




        s = input(f"Ход номер {turn_cnt}, Ходят {turn} : Введите координаты фигуры, которой хотите сходить или напишите Откат для отката назад или нрапишите Подсказка ").split()
        if len(s) == 0:
            continue
        if s[0] == "Стоп":
            break
        if s[0] == "Откат" and len(history_of_game) != 0:
            try:
                otkat = int(input(f"Выберите на сколько ходов вы хотите откатиться (1 - {turn_cnt}) "))
            except ValueError:
                print("Ошибка, неправильный ввод")
                continue
            board = history_of_game[turn_cnt - 1 - otkat]
            turn_cnt -= otkat
            turn = "WHITE" if turn_cnt % 2 else "BLACK"
        if s[0] == "Подсказка":
            pmoves = []
            pcords = []
            if turn == "BLACK":
                for i in range(8):
                    for j in range(8):
                        if board[i][j].isupper():
                            for move in check_moves(j,i):
                                pmoves.append(move)
                        if board[i][j].islower():
                            pcords.append([j,i])
            if turn == "WHITE":
                for i in range(8):
                    for j in range(8):
                        if board[i][j].islower():
                            for move in check_moves(j,i):
                                pmoves.append(move)
                        if board[i][j].isupper():
                            pcords.append([j,i])
            tmp_board = copy.deepcopy(board)
            print("Фигуры, подверженные атаке")
            print("-------------------------")
            for elem in pcords:
                if elem in pmoves:
                    tmp_board[elem[1]][elem[0]] += "+"
                    print(*detranslate_cords(elem[0],elem[1]))
            for i in range(8):
                for j in range(8):
                    if tmp_board[i][j][-1] != "+":
                        tmp_board[i][j] += "-"
            print("--------------------------")
            print("  A  B  C  D  E  F  G  H  ")
            for i, row in enumerate(tmp_board):
                print(8 - i, *row, 8 - i)
            print("  A  B  C  D  E  F  G  H  ")
            print("------------------------------")

            continue
        if len(s) != 2 or s[0] not in letters_to_column or not s[1].isdigit():
            print("Ошибка, проверьте правильность введенных координат")
            continue
        x, y = translate_cords(s[0], int(s[1]))
        if x == -1:
            print("Ошибка, проверьте правильность введенных координат")
            continue
        if board[y][x] == ".":
            print("На этой клетке нет фигур")
            continue
        if (board[y][x].islower() and turn == "WHITE") or (board[y][x].isupper() and turn == "BLACK"):
            print("Ошибка, сейчас ход другого игрока")
            continue
        moves = check_moves(x,y)
        print(moves)
        d = input("Выберите клетку на которую вы хотите сходить или напишите \"Подсказка\" ").split()
        if len(d) == 1 and d[0] == "Подсказка":
            print("Возможные ходы: ")
            tmp_board = copy.deepcopy(board)
            for elem in moves:
                tmp_board[elem[1]][elem[0]] += "+"
                print(*detranslate_cords(elem[0],elem[1]))
            for i in range(8):
                for j in range(8):
                    if tmp_board[i][j][-1] != "+":
                        tmp_board[i][j] += "-"
            print("------------------------------")
            print("  A  B  C  D  E  F  G  H  ")
            for i, row in enumerate(tmp_board):
                print(8 - i, *row, 8 - i)
            print("  A  B  C  D  E  F  G  H  ")
            print("------------------------------")
            d = input("Выберите клетку на которую вы хотите сходить ").split()
        if len(d) != 2 or d[0] not in letters_to_column or not d[1].isdigit():
            print("Ошибка, проверьте правильность введенных координат")
            continue
        x_dest, y_dest = translate_cords(d[0],int(d[1]))
        if x_dest == -1 or [x_dest, y_dest] not in moves:
            print("Ошибка, такой ход невозможен")
            continue
        b_moves = []
        w_moves = []
        bking_coords = []
        wking_coords = []
        for i in range(8):
            for j in range(8):
                if board[i][j].islower():
                    for move in check_moves(j, i):
                        b_moves.append(move)
                if board[i][j].isupper():
                    for move in check_moves(j, i):
                        w_moves.append(move)
                if board[i][j] == "k":
                    bking_coords = [j, i]
                if board[i][j] == "K":
                    wking_coords = [j, i]
        if bking_coords in w_moves and bshah:
            print("Невозможный ход")
            continue
        if wking_coords in b_moves and wshah:
            print("Невозможный ход")
            continue
        bshah = False
        wshah = False
        history_of_game.append(board)
        board[y_dest][x_dest] = board[y][x]
        board[y][x] = "."
        turn = "BLACK" if turn == "WHITE" else "WHITE"
        turn_cnt += 1
        print_board()
if __name__ == "__main__":
    main()