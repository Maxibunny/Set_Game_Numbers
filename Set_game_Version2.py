##from random import randint
##
##
##n = int(input('Введите число >>> '))
##
##P = randint(1, n)  # случайно генерируем число Пети
##print('случайно генерируем число Пети >>> ', P)  # Число Пети
##
##M = set()
##M.add(P)
##nput = 0
##
##restriction = 0
##while restriction < 15 and nput != P and nput == 0:
##    s = input('Введите строку чисел, разделённых пробелами >>> ').split()
##    ss = s.copy()
##    HELP = str(input('Если вам нужна помощь введите "HELP", иначе введите "ENTER" '))
##    #print(HELP)
##    if HELP == 'HELP':
##        print(M)
##    else:
##        s = s[:4]
##        s = set(map(int, s))
##        print(s)
##        
##        if len(s) == 1:
##            ss = s.copy()
##            nput = ss.pop()
##            print('Ваше число >>> ', nput)
##
##        if P in s:
##            M.update(s)
##            print('YES')
##        else:
##            M =  M.defference(s)
##            print('NO')
##
##    restriction += 1  # Счётчик +1, есть 15 попыток
##
##if restriction == 15:
##   print('Ходы закончились(')
##
##if nput == P:
##    print('WIN !!!')
##else:
##    print('YOU LOUSE(( ', a)
##
from random import randint

def playerSet(player):

    Set = player.split()[:4]
    Set = set(map(int, Set))
    return Set


def updateCorrectSet(compNum, corSet, player_):

    plSet = playerSet(player_)
    
    if(compNum in plSet):
        print('You get closer to the right answer :)')
        corSet.update(plSet)
        return corSet
    else:
        print('Computer said you wrong :(')
        corSet = corSet - plSet
        return corSet 
    

def F(player):

    if(player in ['gethelp', 'cheat']):
        return True
    else:
        return len(playerSet(player)) != 1



n = int(input('Computer choose a number from 1 to '))
computerNumber = randint(1, n)
#tryCount = n // 2 + 1
tryCount = 15
correctSet = set()

print()
print(f'У вас {tryCount} попыток')
player = input('Your turn: ')

while(F(player) and tryCount != 1):
    
    if(player == 'gethelp'):
        print(f'Last correct set: {"empty" if len(correctSet) == 0 else correctSet}')
    elif(player == 'cheat'):
        print(f'computerNumber: {computerNumber}')
    else:
        correctSet = updateCorrectSet(computerNumber, correctSet, player)
    
    tryCount -= 1
    print()
    print(f'You have {tryCount} attemps')
    player = input('Your turn: ')

if(player == 'gethelp'):
    print(f'Last correct set: {"empty" if len(correctSet) == 0 else correctSet}')
elif(player == 'cheat'):
    print(f'computerNumber: {computerNumber}')
else:
    updateCorrectSet(computerNumber, correctSet, player)

tryCount -= 1

print()
if(tryCount == 0 or (len(playerSet(player)) == 1 and int(player) != computerNumber)):
    print('Computer win!')
else:
    print('You win!')
