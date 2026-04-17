from turtle import *
import time

t = Turtle()
t.speed(0)

def ret(color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.fd(400)
        t.left(90)
        t.fd(300)
        t.left(90)
    t.end_fill()

def inicio():
    t.ht()
    time.sleep(2)
    t.clear()
    t.pu()
    t.home()
    t.pd()
    t.st()

#JAPÃO
ret('white')
t.pu()
t.goto(200, 80)
t.pd()
t.fillcolor('red')
t.begin_fill()
t.circle(70)
t.end_fill()

inicio()

#SUÍÇA
def cruzsuica(cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.fd(30)
    t.left(90)
    t.fd(60)
    for i in range(3):
        t.right(90)
        t.fd(60)
        t.left(90)
        t.fd(60)
        t.left(90)
        t.fd(60)
    t.right(90)
    t.fd(60)
    t.left(90)
    t.fd(30)
    t.end_fill()

ret('red')
t.pu()
t.goto(200, 60)
t.pd()
cruzsuica('white')


inicio()

#EMIRADOS ARABES UNIDOS
ret('white')
t.fillcolor('black')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.pu()
t.goto(0, 200)
t.pd()
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.pu()
t.home()
t.pd()
t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.left(90)
    t.fd(300)
    t.left(90)
t.end_fill()

inicio()

#BAHAMAS
ret('dark cyan')
t.pu()
t.goto(0, 100)
t.pd()
t.fillcolor('yellow')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.fillcolor('black')
t.begin_fill()
t.pu()
t.home()
t.pd()
t.left(48.59)
t.fd(200)
t.left(82.82)
t.fd(200)
t.home()
t.end_fill()

inicio()

#JORDANIA
ret('white')
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.pu()
t.goto(0, 200)
t.pd()
t.fillcolor('black')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.fillcolor('red')
t.begin_fill()
t.pu()
t.home()
t.pd()
t.left(48.59)
t.fd(200)
t.left(82.82)
t.fd(200)
t.home()
t.end_fill()

inicio()

#LAOS
ret('royal blue')
t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(70)
    t.left(90)
t.end_fill()
t.pu()
t.goto(0, 230)
t.pd()
t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(70)
    t.left(90)
t.end_fill()
t.fillcolor('red')
t.begin_fill()
t.pu()
t.goto(200, 90)
t.pd()
t.fillcolor('white')
t.begin_fill()
t.circle(60)
t.end_fill()

inicio()

#SUDÃO
ret('white')
t.fillcolor('black')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.pu()
t.goto(0, 200)
t.pd()
t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(100)
    t.left(90)
t.end_fill()
t.fillcolor('green')
t.begin_fill()
t.pu()
t.home()
t.pd()
t.left(48.59)
t.fd(200)
t.left(82.82)
t.fd(200)
t.home()
t.end_fill()

inicio()

#NIGER
ret('white')
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(70)
    t.left(90)
t.end_fill()
t.pu()
t.goto(0, 230)
t.pd()
t.fillcolor('orange')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(70)
    t.left(90)
t.end_fill()
t.fillcolor('red')
t.begin_fill()
t.pu()
t.goto(200, 90)
t.pd()
t.fillcolor('orange')
t.begin_fill()
t.circle(60)
t.end_fill()

inicio()

#São Vicente e Granadinas
ret('yellow')
t.fillcolor('royal blue')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.left(90)
    t.fd(300)
    t.left(90)
t.end_fill()
t.pu()
t.goto(300,0)
t.pd()
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.left(90)
    t.fd(300)
    t.left(90)
t.end_fill()
t.pu()
t.goto(200,50)
t.pd()
t.left(60) 
t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.forward(60)
    t.left(60)
    t.forward(60)
    t.left(120)
t.pu()
t.fd(80)
t.pd()
for i in range(2):
    t.forward(60)
    t.left(60)
    t.forward(60)
    t.left(120)
t.pu()
t.backward(80)
t.right(300)
t.fd(80)
t.pd()
for i in range(2):
    t.forward(60)
    t.left(-60)
    t.forward(60)
    t.left(-120)
t.end_fill()

inicio()

#Estados Unidos
ret('white')
t.fillcolor('red')
t.begin_fill()
pos = 0
for i in range(7):
    for i in range(2):
        t.fd(400)
        t.left(90)
        t.fd(23.076)
        t.left(90)
    pos = pos+46.152
    t.pu()
    t.goto(0,pos)
    t.pd()
t.end_fill()
t.pu()
t.home()
t.goto(0,138.45)
t.pd()
t.fillcolor('blue')
t.begin_fill()
for i in range(2):
    t.fd(228)
    t.left(90)
    t.fd(161.55)
    t.left(90)
t.end_fill()
t.pu()
t.goto(8,290)
t.pd()
fil = 290
for i in range(5):
    for i in range(6):
        t.right(18)
        t.fillcolor('white')
        t.begin_fill()
        for i in range(5):
            t.left(18)
            t.fd(5)
            t.left(72)
            t.fd(5)
            t.right(180)
            t.left(18)
        t.end_fill()
        t.left(18)
        t.pu()
        t.fd(40)
        t.pd()
    fil = fil-35
    t.pu()
    t.goto(8,fil)
    t.pd()
t.pu()
t.goto(28,275)
t.pd()
fil = 275
for i in range(4):
    for i in range(5):
        t.right(18)
        t.fillcolor('white')
        t.begin_fill()
        for i in range(5):
            t.left(18)
            t.fd(5)
            t.left(72)
            t.fd(5)
            t.right(180)
            t.left(18)
        t.end_fill()
        t.left(18)
        t.pu()
        t.fd(40)
        t.pd()
    fil = fil-35
    t.pu()
    t.goto(28,fil)
    t.pd()

inicio()


#CAMBODJA
t.pu()
t.goto(-400,-300)
t.pd()

t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.fd(800)
    t.left(90)
    t.fd(600)
    t.left(90)
t.end_fill()

t.fillcolor('medium blue')
t.begin_fill()
for i in range(2):
    t.fd(800)
    t.left(90)
    t.fd(150)
    t.left(90)
t.end_fill()

t.pu()
t.left(90)
t.fd(450)
t.right(90)
t.pd()

t.fillcolor('medium blue')
t.begin_fill()
for i in range(2):
    t.fd(800)
    t.left(90)
    t.fd(150)
    t.left(90)
t.end_fill()

#escada 1 solo 
t.pu()
t.goto(-200,-125)
t.pd()

t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(15)
    t.left(90)
t.end_fill()

#escada 2
t.pu()
t.goto(-195,-110)
t.pd()

t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.fd(390)
    t.left(90)
    t.fd(15)
    t.left(90)
t.end_fill()

#escada 3
t.pu()
t.goto(-190,-95)
t.pd()

t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.fd(380)
    t.left(90)
    t.fd(12.5)
    t.left(90)
t.end_fill()

#escada 4
t.pu()
t.goto(-185,-82.5)
t.pd()

t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.fd(370)
    t.left(90)
    t.fd(10)
    t.left(90)
t.end_fill()

#escada 5
t.pu()
t.goto(-180,-72.5)
t.pd()

t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.fd(360)
    t.left(90)
    t.fd(7.5)
    t.left(90)
t.end_fill()
#fim da escadaria da penha

t.pu()
t.goto(-175,-65)
t.pd()

#base pequena 
t.fillcolor('white')
t.begin_fill()
t.left(45)
t.fd(8)
t.right(45)
t.fd(338.686)
t.right(45)
t.fd(8)
t.left(45)
t.left(180)
t.fd(346.5)
t.end_fill()

t.pu()
t.goto(5,-125)
t.left(180)
t.pd()

def escadademao(x,y):
    t.pu()
    t.home()
    t.goto(x,y)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(5)
        t.left(90)
        t.fd(60)
        t.left(90)

    t.end_fill()

    t.pu()
    t.goto((x+5),y)
    t.pd()

    alt = 7.5
    t.fillcolor('white')
    t.begin_fill()
    for i in range(8):
        for i in range(2):
            t.fd(10)
            t.left(90)
            t.fd(7.5)
            t.left(90)
        t.pu()
        t.goto((x+5),y+alt)
        alt += 7.5
        t.pd()
    t.end_fill()

    t.pu()
    t.goto((x+15),y)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(5)
        t.left(90)
        t.fd(60)
        t.left(90)

    t.end_fill()

    t.pu()
    t.goto((x-35),(y+65.675))
    t.left(90)
    t.pd()

    




escadademao(-10,-125)

escadademao(-135,-125)

escadademao(105,-125)


t.pu()
t.goto(-160,-59.343)
t.pd()

t.fillcolor('white')
t.begin_fill()
for i in range(2):
    t.fd(60)
    t.right(90)
    t.fd(320)
    t.right(90)

t.end_fill()

t.right(90)
t.pu()
t.fd(2)
t.pd()


t.left(90)
for i in range(30):
    t.right(90)
    t.pu()
    t.fd(10)
    t.pd()
    t.left(90)
    for i in range(2):
        t.fd(25)
        t.right(90)
        t.fd(5)
        t.right(90)    

t.pu()
t.goto(-160,-59.343)
t.fd(30)
t.right(90)
t.pd()
t.fd(320)
t.left(90)
t.fd(10)
t.left(90)
t.fd(320)
t.right(90)
t.fd(5)
t.right(90)
t.fd(320)
t.left(90)
t.fd(10)
t.left(90)
t.fd(320)

t.pu()
t.goto(-40,-59.343)
t.right(90)
t.pd()



t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(35)
    t.right(90)
    t.fd(80)
    t.right(90)


t.end_fill()
t.pu()
t.goto(-40,-59.343)
t.pd()

for i in range(7):
    t.right(90)
    t.pu()
    t.fd(11)
    t.pd()
    if i == 0:
        t.backward(7)
    t.left(90)
    for i in range(2):
        t.fd(27)
        t.right(90)
        t.fd(5)
        t.right(90)  
    

t.pu()
t.goto(-27,-59.343)
t.right(90)
t.pd()

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(54)
    t.left(90)
    t.fd(40)
    t.left(90)

t.end_fill()

t.pu()
t.left(90)
t.fd(35)
t.pd()

t.fillcolor('white')
t.begin_fill()

t.fd(5)
t.left(90)
t.fd(10)
t.right(90)
t.fd(40)
t.left(90)
t.fd(5)
t.left(90)
t.fd(45)
t.left(90)
t.fd(15)

t.pu()
t.fd(54)
t.pd()

t.fd(15)
t.left(90)
t.fd(45)
t.left(90)
t.fd(5)
t.left(90)
t.fd(40)
t.right(90)
t.fd(10)
t.left(90)
t.fd(5)

t.end_fill()


t.pu()
t.right(90)
t.backward(10)
t.right(90)
t.fd(5)
t.pd()

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(7)
    t.left(90)
    t.fd(74)
    t.left(90)

t.end_fill()

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(34)
    t.left(90)
    t.fd(5)
    t.left(90)

t.pu()
t.left(90)
t.fd(74)
t.right(90)
t.pd()

for i in range(2):
    t.fd(34)
    t.right(90)
    t.fd(5)
    t.right(90)

t.end_fill()

t.pu()
t.fd(34)
t.right(90)
t.fd(5)
t.pd()

t.fillcolor('white')
t.begin_fill()

t.circle(4, 180)

t.right(90)
t.fd(5)
t.right(90)
for i in range(8):
    t.fd(1)
    t.right(11.25)
t.fd(42)
t.right(90)
t.fd(6)
t.right(90)
t.fd(34)

t.end_fill()

t.pu()
t.backward(34)
t.right(90)
t.fd(64)
t.left(90)
t.fd(34)
t.left(90)
t.pd()

t.fillcolor('white')
t.begin_fill()



t.circle(-4, 180)

t.left(90)
t.fd(5)
t.left(90)
for i in range(8):
    t.fd(1)
    t.left(11.25)
t.fd(43)
t.left(90)
t.fd(6)
t.left(90)
t.fd(34)

t.end_fill()

t.pu()
t.home()
t.goto(0,1)
t.left(90)
t.backward(60)
t.left(90)
t.fd(10)
t.right(90)
t.backward(5.675)
t.pd()

for i in range(2):
    t.fd(35)
    t.right(90)
    t.fd(20)
    t.right(90)


t.end_fill()

t.pu()
t.fd(35)
t.left(90)
t.fd(4)
t.right(90)
t.pd()

for i in range(2):
    t.fd(18)
    t.right(90)
    t.fd(28)
    t.right(90)

t.pu()
t.goto(0,1)
t.right(90)
t.pd()

#####

t.fillcolor('white')
t.begin_fill()

t.fd(26)
t.left(90)
t.fd(35)
t.left(90)
t.fd(5)
t.left(90)
t.fd(20)
t.right(90)
t.fd(42)
t.right(90)
t.fd(20)
t.left(90)
t.fd(5)
t.left(90)
t.fd(35)
t.left(90)
t.fd(26)

t.end_fill()

t.pu()
t.goto(0,16)
t.pd()

t.fillcolor('white')
t.begin_fill()

t.fd(21)
t.left(90)
t.fd(30)
t.left(90)
t.fd(5)
t.left(90)
t.fd(15)
t.right(90)
t.fd(32)
t.right(90)
t.fd(15)
t.left(90)
t.fd(5)
t.left(90)
t.fd(30)
t.left(90)
t.fd(21)

t.end_fill()

t.pu()
t.goto(0,31)
t.pd()

t.fillcolor('white')
t.begin_fill()

t.fd(16)
t.left(90)
t.fd(25)
t.left(90)
t.fd(4)
t.left(90)
t.fd(15)
t.right(90)
t.fd(24)
t.right(90)
t.fd(15)
t.left(90)
t.fd(4)
t.left(90)
t.fd(25)
t.left(90)
t.fd(16)

t.end_fill()

t.pu()
t.goto(0,41)
t.pd()

t.fillcolor('white')
t.begin_fill()

t.fd(12)
t.left(90)
t.fd(20)
t.left(90)
t.fd(24)
t.left(90)
t.fd(20)
t.left(90)
t.fd(12)

t.end_fill()


t.pu()
t.left(90)
t.fd(15)
t.right(90)
t.fd(10)
t.pd()

t.pu()
t.left(90)
t.fd(5)
t.left(90)
t.fd(2)
t.right(90)
t.pd()

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(5)
    t.left(90)
    t.fd(15)
    t.left(90)

t.end_fill()

t.pu()
t.fd(5)
t.left(90)
t.fd(2.5)
t.right(90)
t.pd()

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(5)
    t.left(90)
    t.fd(10)
    t.left(90)

t.end_fill()

t.pu()
t.fd(5)
t.left(90)
t.fd(2.5)
t.right(90)
t.pd()

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(5)
    t.left(90)
    t.fd(5)
    t.left(90)

t.end_fill()

t.pu()
t.fd(5)
t.pd()

t.fillcolor('white')
t.begin_fill()

def torre(x=0,y=0):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(35)
        t.right(90)
        t.fd(80)
        t.right(90)


    t.end_fill()
    t.pu()
    t.goto(x,y)
    t.pd()

    for i in range(7):
        t.right(90)
        t.pu()
        t.fd(11)
        t.pd()
        if i == 0:
            t.backward(7)
        t.left(90)
        for i in range(2):
            t.fd(27)
            t.right(90)
            t.fd(5)
            t.right(90)  
        

    t.pu()
    t.goto((x+13),y)
    t.right(90)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(54)
        t.left(90)
        t.fd(40)
        t.left(90)

    t.end_fill()

    t.pu()
    t.left(90)
    t.fd(35)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    t.fd(5)
    t.left(90)
    t.fd(10)
    t.right(90)
    t.fd(40)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(45)
    t.left(90)
    t.fd(15)

    t.pu()
    t.fd(54)
    t.pd()

    t.fd(15)
    t.left(90)
    t.fd(45)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(40)
    t.right(90)
    t.fd(10)
    t.left(90)
    t.fd(5)

    t.end_fill()


    t.pu()
    t.right(90)
    t.backward(10)
    t.right(90)
    t.fd(5)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(7)
        t.left(90)
        t.fd(74)
        t.left(90)

    t.end_fill()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(34)
        t.left(90)
        t.fd(5)
        t.left(90)

    t.pu()
    t.left(90)
    t.fd(74)
    t.right(90)
    t.pd()

    for i in range(2):
        t.fd(34)
        t.right(90)
        t.fd(5)
        t.right(90)

    t.end_fill()

    t.pu()
    t.fd(34)
    t.right(90)
    t.fd(5)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    t.circle(4, 180)

    t.right(90)
    t.fd(5)
    t.right(90)
    for i in range(8):
        t.fd(1)
        t.right(11.25)
    t.fd(42)
    t.right(90)
    t.fd(6)
    t.right(90)
    t.fd(34)

    t.end_fill()

    t.pu()
    t.backward(34)
    t.right(90)
    t.fd(64)
    t.left(90)
    t.fd(34)
    t.left(90)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()



    t.circle(-4, 180)

    t.left(90)
    t.fd(5)
    t.left(90)
    for i in range(8):
        t.fd(1)
        t.left(11.25)
    t.fd(43)
    t.left(90)
    t.fd(6)
    t.left(90)
    t.fd(34)

    t.end_fill()

    t.pu()
    t.home()
    t.goto((x+30),y)
    t.left(90)
    t.pd()

    for i in range(2):
        t.fd(35)
        t.right(90)
        t.fd(20)
        t.right(90)


    t.end_fill()

    t.pu()
    t.fd(35)
    t.left(90)
    t.fd(4)
    t.right(90)
    t.pd()

    for i in range(2):
        t.fd(18)
        t.right(90)
        t.fd(28)
        t.right(90)


    #retangulos encolhendo dentro

    t.pu()
    t.goto(x+40,y+45)
    t.right(90)
    t.pd()

    #####

    t.fillcolor('white')
    t.begin_fill()

    t.fd(26)
    t.left(90)
    t.fd(35)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(20)
    t.right(90)
    t.fd(42)
    t.right(90)
    t.fd(20)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(35)
    t.left(90)
    t.fd(26)

    t.end_fill()

    t.pu()
    t.goto(x+40,y+45+16)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    t.fd(21)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(32)
    t.right(90)
    t.fd(15)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(30)
    t.left(90)
    t.fd(21)

    t.end_fill()

    t.pu()
    t.goto(x+40,y+45+31)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    t.fd(16)
    t.left(90)
    t.fd(25)
    t.left(90)
    t.fd(4)
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(24)
    t.right(90)
    t.fd(15)
    t.left(90)
    t.fd(4)
    t.left(90)
    t.fd(25)
    t.left(90)
    t.fd(16)

    t.end_fill()

    t.pu()
    t.goto(x+40,y+45+31)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    t.fd(12)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(24)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(12)

    t.end_fill()


    t.pu()
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(10)
    t.pd()

    t.pu()
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(2)
    t.right(90)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(5)
        t.left(90)
        t.fd(15)
        t.left(90)

    t.end_fill()

    t.pu()
    t.fd(5)
    t.left(90)
    t.fd(2.5)
    t.right(90)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(5)
        t.left(90)
        t.fd(10)
        t.left(90)

    t.end_fill()

    t.pu()
    t.fd(5)
    t.left(90)
    t.fd(2.5)
    t.right(90)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()

    for i in range(2):
        t.fd(5)
        t.left(90)
        t.fd(5)
        t.left(90)

    t.end_fill()

    t.pu()
    t.fd(5)
    t.pd()

    t.fillcolor('white')
    t.begin_fill()


torre(-165,-59.343)

torre(75,-59.343)


t.pu()
t.goto(-500,-500)
t.pd()

wd = Screen()
wd.mainloop()
