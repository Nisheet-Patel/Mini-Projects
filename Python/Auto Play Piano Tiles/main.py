# http://www.crazygames.com/game/white-tile-2-don-t-tap-it
# https://kizi.com/games/magic-piano-tiles

import pyautogui as pag
import keyboard
from time import sleep
from os import system

XY = []
COLOR = (0,0,0)  # Black
TOLERANCE = 50

# write XY to coordinates.txt
def write_coordinates():
    with open('coordinates.txt','w') as cord:
        for pos in XY:
            cord.write(f"{int(pos[0])}, {int(pos[1])}\n")
    cord.close()

# Read coordinates.txt and update XY list
def read_coordinates():
    global XY
    XY.clear()
    with open('coordinates.txt','r') as cord:
        for pos in cord.readlines():
            pos = pos.split(',')
            XY.append([int(pos[0]), int(pos[1])])
    cord.close()

# 
def capture_coordinates(mode='new'):
    global XY
    if mode=='new':
        XY.clear()
    while True:
        if keyboard.is_pressed('e'):
            X, Y = pag.position()
            print("Added : x,y = ", X, Y)
            XY.append([X, Y])
            sleep(0.25)
        elif keyboard.is_pressed('q'):
            break
    write_coordinates()

def start():
    while True:
        for i in range(len(XY)):
            if keyboard.is_pressed('q'):
                return           
            elif pag.pixelMatchesColor(XY[i][0], XY[i][1], COLOR, tolerance=TOLERANCE):
                pag.click(XY[i][0], XY[i][1], button='left', clicks=1)
                print(f"Press 'q' to stop | x = {XY[i][0]} | y = {XY[i][1]}")

read_coordinates()
while True:
    system('cls')
    print("coordinates: ",XY)
    print("\n1) New coordinates\n2) Insert coordinates\n3) Start\n0) Exit")
    choice =  input(":")
    if choice == '1':
        print("\nPlace cursur on the piano tile and press 'e' to insert coordinate\npress 'q' when you done\n")
        capture_coordinates()
    elif choice == '2':
        print("\nPlace cursur on the piano tile and press 'e' to insert coordinate\npress 'q' when you done\n")
        capture_coordinates(mode='insert')
    elif choice == '3':
        print("Press 'q' to stop")
        start()
    elif choice == '0':
        break
    else:
        continue
