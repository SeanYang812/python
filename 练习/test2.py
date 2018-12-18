# import turtle
#
# t = turtle.Pen()
# t.shape("turtle")

# a = 8
# b = 3
#
#
# c = a + b
# print("Line 1 - Value of c is ",c)
#
# c = a - b
# print("Line 2 - Value of c is",c)
#
# c = a * b
# print("Line 3 - Value of c is",c)

# print(40 + 200 + 2.5*25)
#
# print((400 - 400/1.2394) * 1.2394)

# import turtle
#
# t = turtle.Pen()
# a = input("请输入你b c d其中的一个字母：")
# if a == "b":
#     for x in range(20):
#         t.circle(90)
#         t.left(18)
# elif a == "c":
#     for x in range(100):
#         t.forward(x)
#         t.right(91)
# elif a == "d":
#     for x in range(100):
#         t.forward(80)
#         t.right(85)

# x = 1
# for i in range(10):
#     x = (x + 1) * 2
# print(x)


import turtle


def draw_diamond1(turt):
    """
    躺着的菱形
    """
    for i in range(1, 3):
        turt.forward(100)  # 向前走100步
        turt.right(135)  # 然后海龟头向右转45度
        turt.forward(100)  # 继续向前走100步
        turt.right(45)  # 然后有向右转135度


def draw_diamond2(turt):
    """
    竖着的菱形
    """
    for i in range(1, 3):
        turt.forward(100)  # 向前走100步
        turt.right(45)  # 然后海龟头向右转45度
        turt.forward(100)  # 继续向前走100步
        turt.right(135)  # 然后有向右转135度


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()  # 创建一个Turtle的实例
    brad.shape("turtle")  # 形状是一个海龟除了画海龟还可以画箭头，圆圈等等
    brad.color("red")  # 颜色是橙色
    brad.speed('fast')  # 画的速度是快速

    for i in range(1, 37):  # 循环36次
        draw_diamond1(brad)#单画一个菱形也就是花瓣
        brad.right(10)  # 旋转10度
        draw_diamond2(brad)
    brad.right(90)  # 当花全部花完一周后，把海龟的头向右转90度
    brad.forward(300)  # 花一根长的线

    window.exitonclick()


draw_art()  # 调用函数