from Player_ai import Human,SmartComputer,rand_computer
import math
class TicTacToe():
    def __init__(self,):
        self.board=[' ' for i in range(9)]
        self.currentwinner=None
    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print('|'.join(row))
          
    def reset(self):
        self.board=[' ' for i in range(9)]
        self.currentwinner=None
    def printNum(self):
        for row in [[str(i) for i in range(j*3,(j+1)*3)]for j in range(3)]:
            print('|'.join(row))
    def makeMove(self,square,letter):
        if self.board[square]==' ':
            self.board[square]=letter
            if self.winner(square,letter):
                self.currentwinner=letter
            return True
        return False
    def winner(self,square,letter):
        #row
        r_ind=math.floor(square/3)
        row=self.board[r_ind*3:(r_ind+1)*3]
        if all([s==letter for s in row]):
            return True
        # col
        c_ind=square%3
        col=[self.board[c_ind +(i*3)]for i in range(3)]
        if all([s==letter for s in col]):
            return True
        #dia
        if square%2==0:
            dia1=[self.board[i] for i in [0,4,8]]
            dia2=[self.board[i] for i in [2,4,6]]
            if all([s==letter for s in dia1]):
                return True
            if all([s==letter for s in dia2]):
                 return True
        return False
    def emptySquare(self):
        return ' ' in self.board
    def emptyNum(self):
        return self.board.count(' ')
    def availMove(self):
        return [num for num,val in enumerate(self.board) if val==' ']
def play(game,x_player,o_player,letsplay=True):
    if letsplay:
        game.printBoard()
        print('-----------------------------------------------------------------------------')
    letter='X'
    while game.emptySquare():
         if letter=='X':
             square=x_player.getMove(game)
         else:
             square=o_player.getMove(game)
         if game.makeMove(square,letter):
            if letsplay:
                game.printBoard()
                print(letter,' have moved to {}'.format(square))
            if game.currentwinner:
                print(letter,' win!!!!!!!!!!')
                game.reset()
                return letter
            letter='O' if letter=='X' else 'X'
    if letsplay:
        game.reset()
        print('its a tie')
if __name__=='__main__':
    game=TicTacToe()
    go=False
    while not go:
        con=input("do want to play game[y/n]")
        if con=='y':
            pickEnemy=input("---------pick your enemy--------\n1.RandomComp(Level 0)\n2.SmartComp(Level 1000)\n\nselect [ 1 or 2 ] ")
            pickLetter=input("---------chose x or o----------\n1.x\n2.o\nselect[1 or 2] ")
            if pickEnemy=='1':
                if pickLetter=='1':
                    x_player=Human('X')
                    o_player=rand_computer('O')
                elif pickLetter=='2':
                    x_player=rand_computer('X') 
                    o_player=Human('O')
                else:
                    print("Invalid input")
                    continue
            elif pickEnemy=='2':
                if pickLetter=='1':
                    x_player=Human('X')
                    o_player=SmartComputer('O') 
                elif pickLetter=='2':
                    x_player=SmartComputer('X') 
                    o_player=Human('O')
                else:
                    print("invaid input")
                    continue
            else:
                print("invalid input")
                continue
        else:
            print("----------------exit-------------------")
            break
        play(game,x_player,o_player,letsplay=True)




                