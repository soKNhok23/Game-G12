import tkinter as tk
import random

root = tk.Tk()
root.geometry('600x600')
frame = tk.Frame()
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)


positionXcarplayer = 200
positionYcarplayer = 200
#function
def carplayer():
    global playercar, positionXcarplayer,positionYcarplayer
    playercar = canvas.create_rectangle(positionXcarplayer ,positionYcarplayer ,positionXcarplayer +30,positionYcarplayer +30 ,fill='blue')

def bullets():
    global gun
    gun = canvas.create_oval(positionXcarplayer,positionYcarplayer,positionXcarplayer+10,positionYcarplayer+10,fill='red',tags = 'bullets_gun')

def move_bullets(event):
    canvas.after(10,move_bullets)
    canvas.move(gun,0,-10)
    

def move_right(event):
    global playercar,positionYcarplayer
    canvas.move(playercar,10,0)

def move_left(event):
    canvas.move(playercar,-10,0)

def move_down(event):
    canvas.move(playercar,0,10)

def move_up(event):
    canvas.move(playercar,0,-10)

def carenemy_yellow():
    global carEnemy_yellow
    postionxcarenemy = random.randrange(1,590)
    carEnemy_yellow = canvas.create_rectangle(postionxcarenemy,0,postionxcarenemy+10,10,fill='yellow')
    canvas.after(10000, carenemy_yellow)

def carenemy_blue():
    global carEnemy_blue
    postionxcarenemy = random.randrange(1,590)
    carEnemy_blue = canvas.create_rectangle(postionxcarenemy,0,postionxcarenemy+10,10,fill='blue')
    canvas.after(12000, carenemy_blue)

def carenemy_red():
    global carEnemy_red
    postionxcarenemy = random.randrange(1,590)
    carEnemy_red = canvas.create_rectangle(postionxcarenemy,0,postionxcarenemy+10,10,fill='red')
    canvas.after(11000, carenemy_red)

def coins():
    global coins_item
    postionxcarenemy = random.randrange(1,590)
    coins_item = canvas.create_oval(postionxcarenemy,0,postionxcarenemy+10,10,fill='orange')
    canvas.after(15000, coins)

def movecarenemydown():
    canvas.move(coins_item,0,0.7)
    canvas.move(carEnemy_yellow,0,1)
    canvas.move(carEnemy_blue,0,1)
    canvas.move(carEnemy_red,0,2)
    canvas.after(5,movecarenemydown)




bullets()
carplayer()
coins()
carenemy_red()   
carenemy_blue()
carenemy_yellow()
movecarenemydown()

    


root.bind('bullets_gun',move_bullets)
root.bind("<d>",move_down)
root.bind("<u>",move_up)
root.bind("<r>",move_right)
root.bind("<l>",move_left)


canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()