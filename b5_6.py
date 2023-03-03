def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

greet()

game_field = [[" "] * 3 for i in range(3) ]

def view_field():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(game_field[i])
        print(f"{i} {game_field[i][0]} {game_field[i][1]} {game_field[i][2]}")
view_field()

def coordinates():
    x, y = map(int, input("         Ваш ход: ").split())
    return x, y
coordinates()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game_field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

game_field = [
    [" ", "X", " "],
    [" ", "X", " "],
    [" ", "X", " "]
]

check_win()

greet()
game_field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    view_field()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    
    x, y = coordinates()
    
    if count % 2 == 1:
        game_field[x][y] = "X"
    else:
        game_field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" Ничья!")
        break