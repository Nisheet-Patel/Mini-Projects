import pygame
import random
from time import sleep
import sys

pygame.init()

screen = pygame.display.set_mode([800,500])

#+---------------------------------------------+
#|                    IMAGE                    |
#+---------------------------------------------+
background = pygame.image.load("img/blackbg.jpg")
#rock_img
rock_img = pygame.image.load("img/rock.png")
rock_rect = rock_img.get_rect(center=(130,380))
#paper_img
paper_img = pygame.image.load("img/paper.png")
paper_rect = paper_img.get_rect(center=(330,380))
#scissor_img
scissor_img = pygame.image.load("img/scissor.png")
scissor_rect = scissor_img.get_rect(center=(530,380))
#rock_hand
rock_hand_L_img = pygame.image.load("img/rock_hand_L.png")
rock_hand_R_img = pygame.image.load("img/rock_hand_R.png")
#paper_hand
paper_hand_L_img = pygame.image.load("img/paper_hand_L.png")
paper_hand_R_img = pygame.image.load("img/paper_hand_R.png")
#scissor_hand
scissor_hand_L_img = pygame.image.load('img/scissor_hand_L.png')
scissor_hand_R_img = pygame.image.load('img/scissor_hand_R.png')
#you_win
you_win_img = pygame.image.load("img/you_win.png")
#you_lose
you_lose_img = pygame.image.load("img/you_lose.png")
#same
same_img = pygame.image.load("img/same.png")
#press_enter
press_enter_img = pygame.image.load("img/press_enter.png")
#end_win
end_win = pygame.image.load('img/end_win.png')
#end_lose
end_lose = pygame.image.load('img/end_lose.png')

#+---------------------------------------------+
#|                    SOUND                    |
#+---------------------------------------------+

win_1 = pygame.mixer.Sound('sound/win.wav')
win_2 = pygame.mixer.Sound('sound/win_1.wav')
lose_sound = pygame.mixer.Sound('sound/lose_sound.wav')
Tie_sound = pygame.mixer.Sound('sound/quack_sound.wav')
button_sound = pygame.mixer.Sound('sound/button_sound.wav')


#+---------------------------------------------+
#|                 VARIABLE                    |
#+---------------------------------------------+
fps = 30
clock = pygame.time.Clock()
white = (255,255,255)


# ......Background Image......
screen.blit(background,[0,0])
pygame.display.update()

#........FONT & TEXT........

def text_on_screen(text,color,size,x,y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])


class Main_a:
    choose_count = 0
    your_s = 0
    bot_s = 0
    game_play_count = 0

    def __init__(self,r_s_p,R_S_P,yh,limg,bg,check=None,xlh=None,xrh=None):
        self.r_s_p = r_s_p
        self.R_S_P = R_S_P
        self.check = check
        self.xlh = 350
        self.xrh = 450
        self.yh = yh
        self.limg = limg
        self.bg = bg

    def update(self):
        self.xlh = (-350)
        self.xrh = 800
        screen.blit(self.bg,[0,0])
        pygame.display.update()

    def user_move(self):
        self.xlh += 350  #xlh --> 0
        screen.blit(self.limg,[self.xlh,self.yh])
        pygame.display.update()
    
    def you_win():
        win_1.play()
        screen.blit(you_win_img,[150,230])
        Main_a.your_s += 1
        Main_a.game_play_count += 1
           
        
    def you_lose():
        lose_sound.play()
        screen.blit(you_lose_img,[150,230])
        Main_a.bot_s += 1
        Main_a.game_play_count += 1

    def press_enter():
        screen.blit(press_enter_img,[530,245])
    
    def both_same():
        Tie_sound.play()
        screen.blit(same_img,[300,230])
        Main_a.game_play_count += 1

    def computer_choose(self):
        item = ["rock","paper","scissor"]
        if Main_a.choose_count <= 5:
            if self.r_s_p == "rock":
                item.remove("rock")
                Main_a.choose_count += 1

            elif self.r_s_p == "paper":
                item.remove("paper")
                Main_a.choose_count += 1

            elif self.r_s_p == "scissor":
                item.remove("scissor")
                Main_a.choose_count += 1

            choose = random.choice(item)
            self.check = choose
            item.append(self.r_s_p)
            print("computer: ",choose)
        else:
            choose = random.choice(item)
            self.check = choose
            print("computer: ",choose)
        

    def algorithm(self):
        if self.check == "rock":
            self.xrh -= 350
            screen.blit(rock_hand_R_img,[self.xrh,self.yh])
            pygame.display.update()
            
            if self.R_S_P == 'S':
                print('You Loss !! :(')
                Main_a.you_lose()
                Main_a.press_enter()
            elif self.R_S_P == 'P':
                print("You Win :)")
                Main_a.you_win()
                Main_a.press_enter()
            else:
                print("Tie")
                Main_a.both_same()
                Main_a.press_enter()
        
        elif self.check == "paper":
            self.xrh -= 350
            screen.blit(paper_hand_R_img,[self.xrh,self.yh])
            pygame.display.update()

            if self.R_S_P == 'R':
                print('You Loss !! :(')
                Main_a.you_lose()
                Main_a.press_enter()
            elif self.R_S_P == 'S':
                print("You Win :)")
                Main_a.you_win()
                Main_a.press_enter()
            else:
                print("Tie")      
                Main_a.both_same()
                Main_a.press_enter()
        
        elif self.check == "scissor":
            self.xrh -= 350
            screen.blit(scissor_hand_R_img,[self.xrh,self.yh])
            pygame.display.update()

            if self.R_S_P == 'P':
                print('You Loss !! :(')
                Main_a.you_lose()
                Main_a.press_enter()
            elif self.R_S_P == 'R':
                print("You Win :)")
                Main_a.you_win()
                Main_a.press_enter()
            else:
                print("Tie")
                Main_a.both_same()
                Main_a.press_enter()  


#-----Object-----#
rock = Main_a("rock","R",20,rock_hand_L_img,background)
paper = Main_a("paper","P",20,paper_hand_L_img,background)
scissor = Main_a("scissor","S",20,scissor_hand_L_img,background)

def main_game():
    screen.blit(background,[0,0])
    pygame.display.update()
    while True:
        screen.blit(rock_img,[50,300])
        screen.blit(paper_img,[250,300])
        screen.blit(scissor_img,[450,300])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rock_rect.collidepoint( event.pos ):
                    button_sound.play()
                    print("You :Rock")
                    sleep(0.1)
                    rock.update()  
                    rock.computer_choose()         
                    rock.algorithm()
                    rock.user_move()

                elif paper_rect.collidepoint( event.pos ):
                    button_sound.play()
                    print("You :Paper")
                    sleep(0.1)
                    paper.update()
                    paper.computer_choose()
                    paper.algorithm()
                    paper.user_move()

                elif scissor_rect.collidepoint( event.pos ):
                    button_sound.play()
                    print("You :Scissor")
                    sleep(0.1)
                    scissor.update()
                    scissor.computer_choose()
                    scissor.algorithm()
                    scissor.user_move()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    rock.update()
        
        text_on_screen("SCORE",white,60,615,320)
        text_on_screen("YOUR : " + str(Main_a.your_s),white,40,630,370)
        text_on_screen("BOT : " + str(Main_a.bot_s),white,40,650,405) 

        text_on_screen("YOU",white,50,30,200)

        pygame.display.update() 
        clock.tick(fps)

        if Main_a.game_play_count == 10:
            sleep(1)
            End_screen()
            break

def End_screen():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    Main_a.game_play_count = 0
                    Main_a.choose_count = 0
                    Main_a.your_s = 0
                    Main_a.bot_s = 0
                    main_game()
                    break

        #---------BackGround----------#
        screen.blit(background,[0,0])

        if Main_a.your_s > Main_a.bot_s:
            screen.blit(end_win,[100,140])
        elif Main_a.your_s < Main_a.bot_s:
            screen.blit(end_lose,[100,140])
        elif Main_a.your_s == Main_a.bot_s:
            screen.blit(same_img,[300,170]) 

        text_on_screen("SCORE",white,100,295,20)
        text_on_screen("YOUR : " + str(Main_a.your_s),white,60,70,100)
        text_on_screen("BOT : " + str(Main_a.bot_s),white,60,580,100) 
        text_on_screen("Press 'Enter'/'Space' to Play Again!",white,50,130,350)
        text_on_screen("Creator: Nisheet Patel",white,30,580,460)

        pygame.display.update() 


#----- MAIN LOOP ------#
main_game()
