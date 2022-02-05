''' 
Game Board  |  Play using number keys

X | O | X            7 | 8 | 9
--+---+--            --+---+--
X | O | O            4 | 5 | 6
--+---+--            --+---+--
X | O | X            1 | 2 | 3
'''

from time import sleep
import os
import msvcrt


class Game:         #Main Game

    a_board = {     # For Output
        1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    

    def __init__(self):
        self.turn = 'X'
        self.X_score = 0
        self.O_score = 0 

    
    
    def Game_Title(self):
        print("""
 _____  _  ____     _____   _____   ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\ /  _  \ /   _\   /__ __\/  _ \/  __/    
  / \  | ||  /       / \   | / \ | |  /       / \  | / \||  \      
  | |  | ||  \_      | |   | |-| | |  \_      | |  | \_/||  /_     
  \_/  \_/\____/     \_/   |_/ \_| \____/     \_/  \____/\____|\
 
 
""")

    def clear_board_value(self):    # clear Move History 
        for i in range(1,10): Game.a_board[i] = ' '
    
    def display_score(self):
        print("X - {}   O - {}\n\n".format(self.X_score, self.O_score).center(20,' '))

    def draw_board(self):       # Output Of Board
        self.display_score()
        print(Game.a_board[7] + ' | ' + Game.a_board[8] + ' | ' + Game.a_board[9])
        print('--+---+--')
        print(Game.a_board[4] + ' | ' + Game.a_board[5] + ' | ' + Game.a_board[6])
        print('--+---+--')
        print(Game.a_board[1] + ' | ' + Game.a_board[2] + ' | ' + Game.a_board[3])
    
    def clear_screen(self):     # clear Screen
        return os.system("cls")

    def Algorithm(self, count):        #check Who Win's
        
        for i in range(3):
           
            # check For Row's
            if (Game.a_board[(1+(i*3))] == Game.a_board[(2+(i*3))] == Game.a_board[(3+(i*3))]) and Game.a_board[(1+(i*3))] != ' ' and count >= 4:
                return (Game.a_board[(1+(i*3))] + " Win's").center(20, '-'), True, Game.a_board[(1+(i*3))]

            # check For Coloumn's
            elif (Game.a_board[(1+(i*1))] == Game.a_board[(4+(i*1))] == Game.a_board[(7+(i*1))]) and Game.a_board[(1+(i*1))] != ' ' and count >= 4:
                return (Game.a_board[(1+(i*1))] + " Win's").center(20, '-'), True, Game.a_board[(1+(i*1))]

            elif (Game.a_board[1] == Game.a_board[5] == Game.a_board[9]) and count >= 4:
                 return (Game.a_board[1] + " Win's").center(20, '-'), True, Game.a_board[1]

            elif (Game.a_board[3] == Game.a_board[5] == Game.a_board[7]) and count >= 4:
                 return (Game.a_board[3] + " Win's").center(20, '-'), True, Game.a_board[3]

            elif i == 2: return False
            
            
def Two_Player():
    player = Game()    

    for o in range(10):

        i = 0
        player.clear_board_value()      # clear Move History 

        while i <= 9:
            player.clear_screen()   # clear a screen
            player.Game_Title()     # Game Title
            player.draw_board()     # Draw Board
            print(("\n {}\'s Turn".format(player.turn)).center(6,' '))
            move = msvcrt.getch()   #input move value
            
            if player.a_board[int(move)] == ' ':            # check available place
                i += 1 
                player.a_board[int(move)] = player.turn     # inscert Value
                if player.turn=='X': 
                    player.turn = 'O'      # change the turn   
                else: player.turn = 'X' 

            else: print("\nThis Place is Already Taken :) --Timer : 2 sec--"), sleep(2.3)
            
            if player.Algorithm(i) != False:
                player.clear_screen()   # clear a screen
                player.Game_Title()     # Game Title
                player.draw_board()     # Draw Board
                print("\n\n" + player.Algorithm(i)[0])

                wins = player.Algorithm(i)[2]
                if 'X' == wins:            # Update Score
                    player.X_score += 1    # add X score
                    player.turn = 'X'
                if 'O' == wins: 
                    player.O_score += 1    # add O score
                    player.turn = 'O'
                break

            if i == 9:                  # Tie 
                player.clear_screen()   # clear a screen
                player.Game_Title()     # Game Title
                player.draw_board()     # Draw Board
                print("Tie".center(6,'-'))
                if player.turn != 'X': player.turn = 'X'
                else: player.turn = 'O'
                break
        sleep(2.5)
    player.clear_screen()
    player.Game_Title()
    player.display_score()
    if player.X_score > player.O_score: print("\n\n~ ~ ~ X Win The Game ~ ~ ~")
    elif player.X_score == player.O_score: print("\n\n~ ~ ~ Tie ~ ~ ~")
    else: print("\n\n~ ~ ~ O Win The Game ~ ~ ~")


if __name__ == '__main__': 
    try:
        Two_Player()
    except: pass
