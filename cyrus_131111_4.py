from random import randint

num = randint(1,2000)
print 'Guess what I think?'
bingo = False

while bingo == False:
    answer = input() #Claim the variable
    
    if answer<num:
        print'too small'
    if answer>num:
        print'too big'
    if answer==num:
        print'BINGO'
        bingo = True
    
