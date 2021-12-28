import tkinter as tk
from winsound import*
import random
import winsound

root = tk.Tk()
root.geometry('1350x890')
frame = tk.Frame()
frame.master.title("Hello PNC")
# root.resizable(False,False)
canvas = tk.Canvas(frame)
canvas = tk.Canvas( root, width = 1350,height =890)
canvas.pack(fill = "both", expand = True)
myPhoto=tk.PhotoImage(file = "img/bg start.png")
img12=tk.PhotoImage(file="img/bg1.png")
img13=tk.PhotoImage(file="img/level.png")
rule1=tk.PhotoImage(file="img/rule_ofgame.png")
car = tk.PhotoImage(file='img/player.png')
car1 = tk.PhotoImage(file='img/car1.png')
car2 = tk.PhotoImage(file='img/car2.png')
car3 = tk.PhotoImage(file='img/car3.png')
coin = tk.PhotoImage(file='img/Coin.png')
num1 = tk.PhotoImage(file='img/num1.png')
num2 = tk.PhotoImage(file='img/num2.png')
num3 = tk.PhotoImage(file='img/num3.png')
text_go = tk.PhotoImage(file='img/tgo.png')
fire = tk.PhotoImage(file='img/fire.png')
gameOver = tk.PhotoImage(file='img/game over.png')
gameWin = tk.PhotoImage(file='img/youwin.png')


#variable 
score = 0 #variable for store global score
life = 5  #variable for store global life
#start game

def startGame():
    # Display image
    canvas.create_image( 0, 0, image = myPhoto,anchor = "nw")
    button1 = tk.Button( root, text = "Exit",command=root.destroy)
    canvas.create_rectangle(400,350,655,420,fill="red",outline="")
    canvas.create_rectangle(695,350,950,420,fill="red",outline="")
    canvas.create_text(822.5,385,text="START",font=('verdana',25,'bold'),tags='start')
    canvas.create_text(527.5,385,text="RULE",font=('verdana',25,'bold'),tags='rule')
    button1.config(height=2, width=10,bg='red')
    winsound .PlaySound("sound\level.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    # Display Buttons
    canvas.create_window( 0, 0, anchor = "nw",window = button1)
startGame()

#Menu of game 
def menu(event):
    canvas.delete("all")
    canvas.create_image(675,445,image=img13)
    canvas.create_text(320,180,text="1",font=('',55,'bold'),tags='play')
    canvas.create_text(550,180,text="2",font=('',55,'bold'),tags='play')
    canvas.create_text(780,180,text="3",font=('',55,'bold'),tags='play')
    canvas.create_text(1010,180,text="4",font=('',55,'bold'),tags='play')
    canvas.create_text(320,315,text="5",font=('',55,'bold'),tags='play')
    canvas.create_text(550,315,text="6",font=('',55,'bold'),tags='play')
    canvas.create_text(780,315,text="7",font=('',55,'bold'),tags='play')
    canvas.create_text(1010,315,text="8",font=('',55,'bold'),tags='play')
    canvas.create_text(320,450,text="9",font=('',55,'bold'),tags='play')
    canvas.create_text(550,450,text="10",font=('',55,'bold'),tags='play')
    canvas.create_text(780,450,text="11",font=('',55,'bold'),tags='play')
    canvas.create_text(1010,450,text="12",font=('',55,'bold'),tags='play')
    canvas.create_text(120,650,text="BACK",font=('verdana',35,'bold'),tags='backFromLevel',fill="white")

#Rule of game
def rule(event):
    canvas.delete("all")
    canvas.create_image(675,445,image=rule1)
    canvas.create_text(190,590,text="BACK",font=('verdana',30,'bold'),tags='backFromRule')
canvas.tag_bind("start","<Button-1>",menu)
canvas.tag_bind("rule","<Button-1>",rule)


# count down number before start game# Create and delete
def de_num3():
    canvas.delete("num3")
    winsound .PlaySound("sound\count down.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

def num_3():
    canvas.create_image(300,150,image=num3,anchor = 'nw',tags="num3")
def de_num2():
    canvas.delete("num2")
def num_2():
    canvas.create_image(300,150,image=num2,anchor = 'nw',tags="num2")
def de_num1():
    canvas.delete("num1")
def num_1():
    canvas.create_image(300,150,image=num1,anchor = 'nw',tags="num1")
def de_tg():
    canvas.delete("tg")
    if life>0 and score<100:
        car_player()
        create_coins()
        create_car1()
        create_car2()
        create_car3()
        displaylf()
        moveDownEn_cn()
        winsound .PlaySound("sound\play.mp3",winsound.SND_FILENAME | winsound.SND_ASYNC)

def tg():
    canvas.create_image(110,150,image= text_go,anchor = 'nw',tags="tg")

#start game after count down number 
def startOurGame(event):
    canvas.create_image(675,445,image=img12)

    button1 = tk.Button( root, text = "Exit",font=20,command=root.destroy)
    button1.config(height=2, width=30,bg='red')
    # Display Buttons
    canvas.create_window( 970, 520, anchor = "nw",window = button1)

    canvas.after(1000,num_3)
    canvas.after(2500,de_num3)
    canvas.after(3500,num_2)
    canvas.after(4500,de_num2)
    canvas.after(5500,num_1)
    canvas.after(6500,de_num1)
    canvas.after(7500,tg)
    canvas.after(8500,de_tg)
    winsound .PlaySound("sound\car.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)



#Function for back to level page
def backForlevel(event):
    startGame()

#Function go to rule page of game
def backForRule(event):
    startGame()

# def backForPlaying(event):
#     menu(event)




#Function For create car player 
def car_player():
    global playerCar
    if life>0 and score<100:
        playerCar = canvas.create_image(350,350, image = car, anchor = 'nw')



#Function for create the coins
def create_coins():
    global coinS 
    if life>0 and score<100:
        coinS = canvas.create_image(random.randrange(110,720),0,image = coin, tags = 'coins')
    canvas.after(9000,create_coins)

# Function for create car enemy1
def create_car1():
    global car_1 
    if life>0 and score<100:
        car_1 = canvas.create_image(random.randrange(110,720),0,image = car1, anchor = 'nw', tags='car_1')
    canvas.after(6000,create_car1)

# Function for create car enemy2
def create_car2():
    global car_2 
    if life>0 and score<100:
        car_2 = canvas.create_image(random.randrange(110,720),0,image = car2,anchor = 'nw', tags='car_2')
    canvas.after(7000,create_car2)

# Function for create car enemy3
def create_car3():
    global car_3 
    if life>0 and score<100:
        car_3 = canvas.create_image(random.randrange(110,720),0,image = car3,anchor = 'nw', tags='car_3')
    canvas.after(8000,create_car3)

#Function move right (move car player)
def move_right(event):
    posiPlayercar = canvas.coords(playerCar)
    positionXPlayercar = posiPlayercar[0]
    if positionXPlayercar<=725:
        canvas.move(playerCar,10,0)
   
#Function move left (move car player)
def move_left(event):
    posiPlayercar = canvas.coords(playerCar)
    positionXPlayercar = posiPlayercar[0]
    if positionXPlayercar>=105:
        canvas.move(playerCar,-10,0)
    
#Function move up (move car player)
def move_up(event):
    posiPlayercar = canvas.coords(playerCar)
    positionYPlayercar = posiPlayercar[1]
    if positionYPlayercar>30:
        canvas.move(playerCar,0,-10)
    
#Function move down (move car player)
def move_down(event):
    posiPlayercar = canvas.coords(playerCar)
    positionYPlayercar = posiPlayercar[1]
    if positionYPlayercar<=550:
        canvas.move(playerCar,0,10)
    
###################################Function for check when car creash each other (coins or car enemy)#####################
def creash():
    global score, life
    positionPlayercar = canvas.coords(playerCar)  #Position car player 
    positionXPlayercar = positionPlayercar[0]
    positionYPlayercar = positionPlayercar[1]
    positioncoinS = canvas.coords(coinS)  #position coins
    positioncar1 = canvas.coords(car_1)    #position car enemy1
    positioncar2 = canvas.coords(car_2)    #position car enemy2
    positioncar3 = canvas.coords(car_3)  #position car enemy3
    if len(positioncoinS)>0 :
        positioncoinSX = positioncoinS[0]
        positioncoinSY = positioncoinS[1]
        if (positionXPlayercar-14 < positioncoinSX and positionXPlayercar +66 > positioncoinSX) and (positioncoinSY>positionYPlayercar and positioncoinSY<positionYPlayercar+80):
            winsound .PlaySound("sound\crahs-coins-mixkit-bonus-earned-in-video-game-2058.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            de_coins()  
            score += 10
            displaysc()
    if len(positioncar1)>0 :
        positionXcar1 = positioncar1[0]
        positionYcar1 = positioncar1[1]
        if (positionXcar1 > positionXPlayercar-50 and positionXcar1 <positionXPlayercar+50) and (positionYcar1 > positionYPlayercar-90 and positionYcar1<positionYPlayercar+30):
            winsound .PlaySound("sound\metCar.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            de_car1()
            life -= 1
            displaylf()
    if len(positioncar2)>0 :
        positionXcar2 = positioncar2[0]
        positionYcar2 = positioncar2[1]
        if (positionXcar2 > positionXPlayercar-50 and positionXcar2 <positionXPlayercar+50) and (positionYcar2 > positionYPlayercar-90  and positionYcar2<positionYPlayercar+30):
            winsound .PlaySound("sound\metCar.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            de_car2()
            life -= 1
            displaylf()
    if len(positioncar3)>0 and score<100 and life>0:
        positioncar3X = positioncar3[0]
        positioncar3Y = positioncar3[1]
        if (positioncar3X > positionXPlayercar-50 and positioncar3X <positionXPlayercar+50) and (positioncar3Y > positionYPlayercar-90  and positioncar3Y<positionYPlayercar+30):
            winsound .PlaySound("sound\metCar.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            de_car3()
            life -= 1
            displaylf()
    elif score==100:
        canvas.delete('all')
        winsound .PlaySound("sound\gameOver.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        canvas.create_image(0,0,image=gameWin,anchor = 'nw',tags="num1")
        # canvas.create_text(120,650,text="BACK",font=('verdana',35,'bold'),tags='backForPlaying',fill="white")

    elif life==0:
        canvas.delete('all')
        winsound .PlaySound("sound\gameOver.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        canvas.create_image(0,0,image=gameOver,anchor = 'nw',tags="num1")
        notLostOrWin=False


#Function for move car enemy and coins down 
def moveDownEn_cn():
    canvas.move(coinS,0,2)
    canvas.move(car_1,0,2)
    canvas.move(car_2,0,3)
    canvas.move(car_3,0,4)

    creash()
    #we check if the position of coins or car enemy more than 590 we will delete it 
    posicoins = canvas.coords(coinS)
    posicEn1 = canvas.coords(car_1)
    posicEn2 = canvas.coords(car_2)
    posicEn3 = canvas.coords(car_3)
    if len(posicoins)>0:
        if posicoins[1]>590:
            canvas.delete('coins')
    if len(posicEn1)>0:
        if posicEn1[1]>590:    
            canvas.delete('car_1')
    if len(posicEn2)>0:
        if posicEn2[1]>590:    
            canvas.delete('car_2')
    if len(posicEn3)>0:
        if posicEn3[1]>590:    
            canvas.delete('car_3')
    canvas.after(10,moveDownEn_cn)


#Function for create text score that display on screen
def displaysc():
    canvas.delete('socre')
    canvas.create_text(1100,170,font=('',30),text=score,tags= "socre")

#Funcetion for create text life that display on screen
def displaylf():
    canvas.delete('life')
    canvas.create_text(1100,285,font=('',30),text=life,tags= "life")


#Function for delete coins and care enemy when car player creash them
def de_coins():
    canvas.delete(coinS)
def de_car1():
    canvas.delete( car_1)
def de_car2():
    canvas.delete(car_2)
def de_car3():
    canvas.delete(car_3)
#Key event
canvas.tag_bind("play","<Button-1>",startOurGame)             
canvas.tag_bind("backFromLevel","<Button-1>",backForlevel)    #key for move from one page to one page
canvas.tag_bind("backFromRule","<Button-1>",backForRule)
#=========================================================
# canvas.tag_bind("backForPlaying","<Button-1>",backForPlaying)



root.bind('d',move_down)  
root.bind('e',move_up)    
root.bind('<f>',move_right)  # key for move car player 
root.bind('<s>',move_left) 

canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()

