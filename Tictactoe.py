#define variables
from IPython.display import clear_output
def define():
    global border, line, one, four, seven, mode, turn, win, XorO, winlose, winn, entered_value
    border = []
    line = []
    one = []
    four = []
    seven = []
    mode = True
    turn = True
    win = False
    XorO = True
    entered_value = []
    winlose ={'1':[],'2':[]}
    winn = [['1','2','3'],['4','5','6'],['7','8','9'],['1','5','9'],['3','5','7'],['1','4','7'],['2','5','8'],['3','6','9']]
    #define borderlines
    for a in "|---|---|---|":
        border.append(a)
    for a in "|   |   |   |":
        line.append(a)
        one.append(a)
        four.append(a)
        seven.append(a)
#define game body
def gameplay():
    define()
    global turn, win, entered_value
    #game start 
    game_interface()
    board()
    #Iteration
    while not win:
        if winorlose():
            if XorO:
                print('X win!')
                break
            else:
                print('O win!')
                break
        elif len(winlose['1']) + len(winlose['2']) == 9:
            print('Deuce!')
            break
        else:
            pass
        step()
        player_input = input()
        while player_input in entered_value:
            print('Invalid value')
            player_input = input()
        entered_value.append(player_input)
        replace(player_input)
        if turn == True:
            winlose['1'].append(player_input)
        else:
            winlose['2'].append(player_input)
        clear_output()
        board()
        turn = not turn
    replay()    
def board():
    print("".join(a for a in border))
    print("".join(a for a in seven)) 
    print("".join(a for a in border))
    print("".join(a for a in four))
    print("".join(a for a in border))
    print("".join(a for a in one))
    print("".join(a for a in border))
def game_interface():
    global mode
    XorO = input("You want to be X or 0? ")
    if XorO in ["X","x"]:
        clear_output()
        return print("X will go first!")
    else: 
        clear_output()
        mode = False
        return print("O will go first!")     
def replay():
    rep = input("Wanna replay? ")
    if rep in ["Yes","yes","y","Y"]:
        gameplay()
    else:
        return 
def step():
    global turn
    if mode == True and turn == True:
        return print("It's X's turn")
    elif mode == True and turn == False:
        return print("It's O's turn")
    elif mode == False and turn == True:
        return print("It's O's turn")
    elif mode == False and turn == False:
        return print("It's X's turn")
def replace(num):
    #X first
    if mode == True:
        if turn == True :
            if num in ["1","2","3"]:
                if num == "1":
                    one[2] = "X"
                elif num == "2":
                    one[6] = "X"
                else:
                    one[10] = "X"
            elif num in ["4","5","6"]:
                if num == "4":
                    four[2] = "X"
                elif num == "5":
                    four[6] = "X"
                else:
                    four[10] = "X"
            else:
                if num == "7":
                    seven[2] = "X"
                elif num == "8":
                    seven[6] = "X"
                else:
                    seven[10] = "X"
        else:
            if num in ["1","2","3"]:
                if num == "1":
                    one[2] = "O"
                elif num == "2":
                    one[6] = "O"
                else:
                    one[10] = "O"
            elif num in ["4","5","6"]:
                if num == "4":
                    four[2] = "O"
                elif num == "5":
                    four[6] = "O"
                else:
                    four[10] = "0"
            else:
                if num == "7":
                    seven[2] == "O"
                elif num == "8":
                    seven[6] = "O"
                else:
                    seven[10] = "O"
    else: # O first
        if turn == True:
            if num in ["1","2","3"]:
                if num == "1":
                    one[2] = "O"
                elif num == "2":
                    one[6] = "O"
                else:
                    one[10] = "O"
            elif num in ["4","5","6"]:
                if num == "4":
                    four[2] = "O"
                elif num == "5":
                    four[6] = "O"
                else:
                    four[10] = "O"
            else:
                if num == "7":
                    seven[2] = "O"
                elif num == "8":
                    seven[6] = "O"
                else:
                    seven[10] = "O"
        else:
            if num in ["1","2","3"]:
                if num == "1":
                    one[2] = "X"
                elif num == "2":
                    one[6] = "X"
                else:
                    one[10] = "X"
            elif num in ["4","5","6"]:
                if num == "4":
                    four[2] = "X"
                elif num == "5":
                    four[6] = "X"
                else:
                    four[10] = "X"
            else:
                if num == "7":
                    seven[2] = "X"
                elif num == "8":
                    seven[6] = "X"
                else:
                    seven[10] = "X"
def winorlose():
    global XorO
    if winlose['1'] in winn:
        return True 
    elif winlose['2'] in winn:
        XorO = False
        return True 