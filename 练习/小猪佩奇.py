# from turtle import *
#
#
# def nose(x, y):  # 鼻子
#     penup()  # 提起笔
#     goto(x, y)  # 定位
#     pendown()  # 落笔，开始画
#     setheading(-30)  # 将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
#     begin_fill()  # 准备开始填充图形
#     speed('fast')
#     a = 0.4
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a = a + 0.08
#             left(3)  # 向左转3度
#             forward(a)  # 向前走a的步长
#         else:
#             a = a - 0.08
#             left(3)
#             forward(a)
#     end_fill()  # 填充完成
#     penup()
#     setheading(90)
#     forward(25)
#     setheading(0)
#     forward(10)
#     pendown()
#     pencolor(255, 155, 192)  # 画笔颜色
#     setheading(10)
#     begin_fill()
#     circle(5)
#     color(160, 82, 45)  # 返回或设置pencolor和fillcolor
#     end_fill()
#     penup()
#     setheading(0)
#     forward(20)
#     pendown()
#     pencolor(255, 155, 192)
#     setheading(10)
#     begin_fill()
#     circle(5)
#     color(160, 82, 45)
#     end_fill()
#
#
# def head(x, y):  # 头
#     color((255, 155, 192), "pink")
#     penup()
#     goto(x, y)
#     setheading(0)
#     pendown()
#     begin_fill()
#     setheading(180)
#     circle(300, -30)
#     circle(100, -60)
#     circle(80, -100)
#     circle(150, -20)
#     circle(60, -95)
#     setheading(161)
#     circle(-300, 15)
#     penup()
#     goto(-100, 100)
#     pendown()
#     setheading(-30)
#     a = 0.4
#     for i in range(60):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a = a + 0.08
#             lt(3)  # 向左转3度
#             fd(a)  # 向前走a的步长
#         else:
#             a = a - 0.08
#             lt(3)
#             fd(a)
#     end_fill()
#
#
# def ears(x, y):  # 耳朵
#     color((255, 155, 192), "pink")
#     penup()
#     goto(x, y)
#     pendown()
#     begin_fill()
#     setheading(100)
#     circle(-50, 50)
#     circle(-10, 120)
#     circle(-50, 54)
#     end_fill()
#     penup()
#     setheading(90)
#     forward(-12)
#     setheading(0)
#     forward(30)
#     pendown()
#     begin_fill()
#     setheading(100)
#     circle(-50, 50)
#     circle(-10, 120)
#     circle(-50, 56)
#     end_fill()
#
#
# def eyes(x, y):  # 眼睛
#     color((255, 155, 192), "white")
#     penup()
#     setheading(90)
#     forward(-20)
#     setheading(0)
#     forward(-95)
#     pendown()
#     begin_fill()
#     circle(15)
#     end_fill()
#     color("black")
#     penup()
#     setheading(90)
#     forward(12)
#     setheading(0)
#     forward(-3)
#     pendown()
#     begin_fill()
#     circle(3)
#     end_fill()
#     color((255, 155, 192), "white")
#     penup()
#     seth(90)
#     forward(-25)
#     seth(0)
#     forward(40)
#     pendown()
#     begin_fill()
#     circle(15)
#     end_fill()
#     color("black")
#     penup()
#     setheading(90)
#     forward(12)
#     setheading(0)
#     forward(-3)
#     pendown()
#     begin_fill()
#     circle(3)
#     end_fill()
#
#
# def cheek(x, y):  # 腮
#     color((255, 155, 192))
#     penup()
#     goto(x, y)
#     pendown()
#     setheading(0)
#     begin_fill()
#     circle(30)
#     end_fill()
#
#
# def mouth(x, y):  # 嘴
#     color(239, 69, 19)
#     penup()
#     goto(x, y)
#     pendown()
#     setheading(-80)
#     circle(30, 40)
#     circle(40, 80)
#
#
# def body(x, y):
#     """
#     身体
#     :param x:
#     :param y:
#     :return:
#     """
#     color("red", (255, 99, 71))
#     pu()
#     seth(90)
#     fd(-20)
#     seth(0)
#     fd(-78)
#     pd()
#     begin_fill()
#     seth(-130)
#     circle(100, 10)
#     circle(300, 30)
#     seth(0)
#     fd(230)
#     seth(90)
#     circle(300, 30)
#     circle(100, 3)
#     color((255, 155, 192), (255, 100, 100))
#     seth(-135)
#     circle(-80, 63)
#     circle(-150, 24)
#     end_fill()
#
#
# def hand(x, y):
#     color((255, 155, 192))
#     pu()
#     seth(90)
#     fd(-40)
#     seth(0)
#     fd(-27)
#     pd()
#     seth(-160)
#     circle(300, 15)
#     pu()
#     seth(90)
#     fd(15)
#     seth(0)
#     fd(0)
#     pd()
#     seth(-10)
#     circle(-20, 90)
#     pu()
#     seth(90)
#     fd(30)
#     seth(0)
#     fd(237)
#     pd()
#     seth(-20)
#     circle(-300, 15)
#     pu()
#     seth(90)
#     fd(20)
#     seth(0)
#     fd(0)
#     pd()
#     seth(-170)
#     circle(20, 90)
#
# def setting():  # 参数设置
#     pensize(4)
#     hideturtle()  # 使乌龟无形（隐藏）
#     colormode(255)  # 将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
#     color((255, 155, 192), "pink")
#     setup(840, 500)
#     speed(10)
#
#
# def main():
#     setting()  # 画布、画笔设置
#     nose(-100, 100)  # 鼻子
#     head(-69, 167)  # 头
#     ears(0, 160)  # 耳朵
#     eyes(0, 140)  # 眼睛
#     cheek(80, 10)  # 腮
#     mouth(-20, 30)  # 嘴
#     body(-5, -20)
#     hand()
#     done()
#
#
# if __name__ == '__main__':
#     main()
#
# # 手
# t.color((255, 155, 192))
# t.pu()
# t.seth(90)
# t.fd(-40)
# t.seth(0)
# t.fd(-27)
# t.pd()
# t.seth(-160)
# t.circle(300, 15)
# t.pu()
# t.seth(90)
# t.fd(15)
# t.seth(0)
# t.fd(0)
# t.pd()
# t.seth(-10)
# t.circle(-20, 90)
# t.pu()
# t.seth(90)
# t.fd(30)
# t.seth(0)
# t.fd(237)
# t.pd()
# t.seth(-20)
# t.circle(-300, 15)
# t.pu()
# t.seth(90)
# t.fd(20)
# t.seth(0)
# t.fd(0)
# t.pd()
# t.seth(-170)
# t.circle(20,90)
# # 脚
# t.pensize(10)
# t.color((240, 128, 128))
# t.pu()
# t.seth(90)
# t.fd(-75)
# t.seth(0)
# t.fd(-180)
# t.pd()
# t.seth(-90)
# t.fd(40)
# t.seth(-180)
# t.color("black")
# t.pensize(15)
# t.fd(20)
# t.pensize(10)
# t.color((240, 128, 128))
# t.pu()
# t.seth(90)
# t.fd(40)
# t.seth(0)
# t.fd(90)
# t.pd()
# t.seth(-90)
# t.fd(40)
# t.seth(-180)
# t.color("black")
# t.pensize(15)
# t.fd(20)
# # 尾巴
# t.pensize(4)
# t.color((255, 155, 192))
# t.pu()
# t.seth(90)
# t.fd(70)
# t.seth(0)
# t.fd(95)
# t.pd()
# t.seth(0)
# t.circle(70, 20)
# t.circle(10, 330)
# t.circle(70, 30)
# t.done()


# import turtle
#
# t = turtle.Pen()
# turtle.bgcolor("black")
# my_name = turtle.textinput("输入你的姓名", "你的名字？")
# colors = ["red", "yellow", "purple", "blue"]
# for x in range(100):
#     t.pencolor(colors[x % 4])
#     t.penup()
#     t.forward(x * 4)
#     t.pendown()
#     t.write(my_name, font=("Arial", int((x + 4) / 4), "bold"))
#     t.left(92)

