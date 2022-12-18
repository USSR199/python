import os 

os.system('cls')

def Truth ():
    result = True

    for n in range(0, 8):
        num = bin(n)
        num = num.replace('b', '0')
        X = int(num[-3])
        Y = int(num[-2])
        Z = int(num[-1])
        result = result and (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))

    print(result)


Truth()
