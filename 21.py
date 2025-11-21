import random

name = input("name:") 
fscore = 0
in_game = True

def roll():
    global fscore, in_game
    rolls = random.randint(1, 6)
    fscore += rolls
    score = fscore
    if score > 21:
        score = 0
        in_game = False
    return rolls, score
    


while in_game:
    rolls, score = roll()
    print(f"you roll {rolls} your score is {score}")
    if in_game:
        keep = input("[y/n]:")
        if keep in 'n':
            in_game = False

print("you ")       
print(fscore)

bfscore = 0
Bin_game = True

def broll():
    global bfscore, Bin_game
    brolls = random.randint(1, 6)
    bfscore += brolls
    bscore = bfscore
    if bscore > 21:
        #bscore = 0
        Bin_game = False
    return brolls, bscore

while in_game:
    brolls, bscore = broll()
    if in_game:
        if bscore >= score:
            Bin_game = False

print("bot ") 
print(bfscore)
    
    
    