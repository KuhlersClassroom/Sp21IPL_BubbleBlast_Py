from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
windowtitle('Bubble Blaster')
c = Canvas(window, width=WIDTH, hight=HIGHT, bg= 'darkblue')
ship_id =c.create_polygon (5,5,5,25,30,15, fill = 'red')
ship_id2 = c.create_oval (0,0,30,30, outline ='red')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move (ship_id, MID_X, MID_Y)
c.move (Ship_id2, MID_X, MID_Y)
SHIP_SPEED = 10
def move_ship (event):
    if event.keysym == 'Up':
        c.move (ship_id, 0,-SHIP_SPEED)
        c.move (ship_id2, 0,-SHIP_SPEED)
    elif event.keysym == 'Down':
        c.move (ship_id, 0,SHIP_SPEED)
        c.move (ship_id2, 0,SHIP_SPEED)
    elif event.keysym == 'Left':
        c.move (ship_id,-SHIP_SPEED, 0)
        c.move (ship_id2,-SHIP_SPEED, 0)
    elif event.keysym == 'Right':
        c.move (ship_id, SHIP_SPEED, 0)
        c.move (ship_id2, SHIP_SPEED, 0)
c.bind_all('<Key>', move_ship)

from random import randint
bub_id = list()
bub_r = list()
