import random

class Player:
    def __init__(self, name,): 
        self.name = name
        self.total = 0
        self.in_game = True


    def roll(self):
        rolls = random.randint(1, 6)
        self.score += rolls
        score = self.score
        if self.score > 21:
            self.score = 0
            self.in_game = False
        return rolls, score
    
p1 = Player(input("name"))
p2 = Player(input("name"))

while p1.in_game or p2.in_game:
    for p in (p1, p2):
        if p.in_game:
            rolls, score = p.roll()
            print(f"{p.name}you roll {rolls} your score is {score}")
            if p.in_game:
                keep = input("[y/n]:")
                if keep in 'n':
                    p.in_game = False

