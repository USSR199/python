lst = list(range(1, 10))

victoria = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def grid(lst):
    print('-'* 13)
    for i in range(3):
        print('|', lst[0 + i*3], '|', lst[1 + i*3], '|', lst[2 + i*3], '|')
        print('-'* 13)

def step_grid(step,symbol):
    ind = lst.index(step)
    lst[ind] = symbol

def result():
    win = ""
 
    for i in victoria:
        if lst[i[0]] == "X" and lst[i[1]] == "X" and lst[i[2]] == "X":
            win = "X"
        if lst[i[0]] == "O" and lst[i[1]] == "O" and lst[i[2]] == "O":
            win = "O"   
             
    return win

def game(lst):
    game_over = False
    player1 = True
    
    while game_over == False:
    
        grid(lst)
    
        if player1 == True:
            symbol = "X"
            step = int(input("Игрок 1, ваш ход: "))
            if step < 1 or step > 9:
                step = int(input("Уверен? Попробуй ещё раз: "))
        else:
            symbol = "O"
            step = int(input("Игрок 2, ваш ход: "))
            if step < 1 or step > 9:
                step = int(input("Уверен? Попробуй ещё раз: "))
    
        step_grid(step,symbol)
        win = result()
        if win != "":
            game_over = True
        else:
            game_over = False
    
        player1 = not(player1)        
    
    grid(lst)
    print("Победил", win) 
game(lst)
