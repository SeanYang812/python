# n = 50
# from turtle import *
#
# speed("fastest")
# left(90)
# forward(3*n)
# color("orange", "yellow")
# begin_fill()
# left(126)
# for i in range(5):
#     forward(n/5)
#     right(144)
# forward(n/5)
# left(72)
# end_fill()
# right(126)
# color("dark green")
# backward(n*4.8)
# def tree(d, s):
#     if d <= 0:
#         return
#     forward(s)
#     tree(d-1, s*.8)
#     right(120)
#     tree(d-3, s*.5)
#     right(120)
#     tree(d-3, s*.5)
#     right(120)
#     backward(s)
#     tree(15, n)
#     backward(n/2)
#
# tree(10,50)


# import turtle
#
# t = turtle.Pen()
#
# t.shape("turtle")
# n = 50
# t.speed("fastest")
# t.left(90)
# t.forward(3 * n)
# t.color("orange", "yellow")
# t.begin_fill()
# t.left(126)
#
# for i in range(5):
#     t.forward(n/5)
#     t.right(144)
#     t.forward(n/5)
#     t.left(72)
# t.end_fill()
# t.right(126)
# t.color("dark green")
# t.backward(n*4.8)
#
# def tree(d, s):
#     if d <= 0:
#         return
#
#     t.forward(s)
#     tree(d-1, s*8)
#     t.right(120)
#     tree(d-3, s*5)
#     t.right(120)
#     tree(d-3, s*5)
#     t.right(120)
#     t.backward(s)
#     tree(15, n)
#     t.backward(n/2)
#
# tree(50,100)


import turtle, datetime
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()
main()












