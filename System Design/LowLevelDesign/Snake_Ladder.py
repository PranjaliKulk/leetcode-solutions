import random

class Player:
    def __init__(self, name):
        self.name = name # Player name
        self.position = 0 # Player position

class Snake:
    def __init__(self, start, end):
        self.start = start  # Snake Head
        self.end = end # Snake Tail

class Ladder:
    def __init__(self, start,end):
        self.start = start # Ladder Head
        self.end = end # Ladder Tail
    
class Dice:
    def roll(self):
        return random.randint(1,6) # Imports Random libarary and returns a random number from 1 to 6
    
class Board:
    def __init__(self, size, snakes, ladders):
        self.size = size # Board size eg 100
        self.snakes = {s.start: s.end for s in snakes} # Map snake head to tail
        self.ladders = {l.start: l.end for l in ladders} # Map ladder start to end

    def get_position(self, pos):
        if pos in pos.snakes:
            return self.snakes[pos]
        if pos in pos.ladders:
            return self.ladders[pos]
        return pos
    
class Game:
    def __init__(self, players, board, dice):
        self.players = players
        self.board = board
        self.dice = Dice()

    def play(self):
        while True: # Looping until a player wins
            for player in self.palyers:
                roll = self.dice.roll() # roll dice to get values bet 1 to 6

                next_pos = player.position + roll # Calculate tentative next position

                if next_pos > self.board.size:
                    continue

                final_pos = self.board.get_next_position(next_pos)

                player.position = final_pos

                if final_pos == self.board.size:
                    print(f"{player.name} wins!")
                    return















    