import random
import math


class Player():
    def __init__(self, letter):
        self.letter = letter

    def getMove(self, game):
        pass

class rand_computer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    def getMove(self,game):
        square=random.choice(game.availMove())
        return square

class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        valid = False
        val = None
        while not valid:
            try:
                val = int(input(f"{self.letter} enter the vaid move [0-8]"))
                if val not in game.availMove():
                    raise ValueError
                valid = True
            except (ValueError):
                print('invalid move try again')
        return val


class SmartComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, game):
        if len(game.availMove()) == 9:
            square=int(random.choice([0, 2, 6, 8]))
        else:
            square= self.minMax(game, self.letter)['position']
        return square

    def minMax(self, state, player):
        max_player = self.letter
        prev_player = 'X' if player == 'O' else 'O'
        if state.currentwinner == prev_player:
            return {'position': None, 'utility': 1*(state.emptyNum()+1)if prev_player==max_player else -1*(state.emptyNum()+1)}
        elif not state.emptySquare():
            return {'position': None, 'utility': 0}
        if player == max_player:
            best = {'position': None, 'utility': -math.inf}
        else:
            best = {'position': None, 'utility': math.inf}
        for possi in state.availMove():
            state.makeMove(possi,player)
            sim_uti = self.minMax(state, prev_player)
            state.board[possi] = ' '
            state.currentwinner = None
            sim_uti['position'] = possi
            if player == max_player:
                if sim_uti['utility'] > best['utility']:
                    best = sim_uti
            else:
                if sim_uti['utility'] < best['utility']:
                    best = sim_uti
        return best
