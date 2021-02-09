from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
window.tittle('Bubble b]Blaster')
c = Canvas(window, Width=WIDTH, height=HEIGHT, bg= 'darkblue')
c,pack()
ship_id = c.Create_polygon (5,5,5,25,30,15, fill = 'red')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move (ship_id, MID_X, MID_Y)
c.move (Ship_id2, MID_X, MID_Y)
ShIP_FEED = 10
def move_ship (event):
    if event.keysym == 'Up':
        c.move (ship_id, 0,-SHIP_SPEED)
        c.move (Ship_id2, 0,-SHIP_SPEED)
    elif event.keysm == 'Down':
        c.move (ship_id, 0,-SHIP_SPEED)
        c.move (Ship_id2, 0.-SHIP_SPEED)
    elif event.keysm == 'Left':
        c.move (Ship_id, 0,-SHIP_SPEED, 0)
        c.move (Ship_id2, 0,-SHIP_SPEED, 0)
    elif event.keysm == 'Roght':
        c.move (Ship_id, 0,-SHIP_SPEED, 0)
        c.move (Ship_id2, 0,-SHIP_SPEED, 0)
c.bind_all('<Key>', move_ship)

from random import randint
bub_id = list()
bub_r = list()
bub_speeed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100
def creative_bubble():
    x = WIDTH + GAP
    y = randint(0,HEIGHT)
    r randint(MIN_BUB_R, MAX_BUB_R)
    idl = c.create_oval(x-r, y-r, x+r, Y+r, outline = 'white')
    



