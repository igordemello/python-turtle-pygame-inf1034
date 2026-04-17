from turtle import *
import math
import time

t = Turtle()
t2 = Turtle()
t.speed(0)
t2.speed(0)

def planocartesiano():
    t2.pu()
    t2.home()
    t2.pd()
    t2.fd(400)
    t2.stamp()
    t2.backward(800)
    t2.fd(400)
    t2.left(90)
    t2.fd(400)
    t2.stamp()
    t2.backward(800)
    t2.pu()
    t2.home()
    t2.pd()
    t2.hideturtle()

#y = √x
def raiz(x):
    return math.sqrt(x)


#y = 1/x
def um_sobre(x):
    if(x==0): return 0
    return(1/x)

#y = 2^x
def dois_elevado(x):
    return(2**x)

#y = 5 - x^2
def cinco_menos_x_quadrado(x):
    return(5-(x**2))


#y = x^2 - 5x + 6
def x_ao_quadrado_menos_cincox_mais_seis(x):
    return((x**2)-(5*x+6))

#y = x^3 - x^2 - x + 1
def x_a_terceira_menos_x_ao_quadrado_etc(x):
    return((x**3)-(x**2)-(x+1))

def desenhar_funcao(x, funcao, x2,cor,escala,escalay):
    t.color(cor)
    t.pu()
    t.home()
    t.goto(x*escala,funcao(x)*escalay)
    t.pd()
    for x in range(x,x2):
        if funcao == um_sobre:
            if x == 0 and funcao(x)*escala == 0 or x == 1:
                t.pu()
            else: t.pd()
        t.goto(x*escala,funcao(x)*escalay)
        print(x*escala,funcao(x)*escalay)
    time.sleep(2)
    t.clear()


planocartesiano()

desenhar_funcao(0,raiz,10,'red',50,50)

desenhar_funcao(-50,um_sobre,50,'red',5,300)

desenhar_funcao(-10,dois_elevado,10,'red',20,20)

desenhar_funcao(-10,cinco_menos_x_quadrado,10,'red',20,20)

desenhar_funcao(-10,x_ao_quadrado_menos_cincox_mais_seis,10,'red',10,10)

desenhar_funcao(-10,x_a_terceira_menos_x_ao_quadrado_etc,10,'red',10,10)



wd = Screen()
wd.mainloop()