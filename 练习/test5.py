
# age = int(input("输入年龄："))
# grade = int(input("输入你的年级:"))
# if age > 10:
#     if grade > 3:
#          print("你可以玩游戏了，请注意时间哦")
#     else:
#         print("不可以")
# else:
#     print("对不起，你还不能玩游戏哦")


# password = "123456"
# a = 0
# while a < 3:
#     c = 2-a
#     b = input("请输入密码")
#     if b == password:
#         print("密码正确")
#         a=3
#     else:
#         if c == 0:
#             print("支付宝账号已锁定！")
#             a=3
#         else:
#             print("密码错误,还剩",c,"次机会")
#     a+=1

# password = "123"
# count = 0
# while count < 3:
#     pwd = input("请输入你的密码：").strip()
#     if password == pwd:
#         print("恭喜您，支付成功！！！")
#         break
#     else:
#         if count == 2:
#             print("该账户已锁定")
#         else:
#             print("密码错误，还剩",2 - int(count),"次机会")
#     count += 1

# print("hello",input(">>>>:").strip(),"ssss")

# name = input("你是谁：").strip()
# name1 = input("》》》：")
# print(name == name1)

# try:
#     num = int(float(input(">>>>:")))
#     print(num)
# except Exception as e:
#     print(e)
# a = 1
# b = 2
# a,b = b,a

#
head = int(input("一共几个头:"))
leg = int(input("一共几条腿:"))
for chicken in range(0, head + 1):
    rabbit = head - chicken
    if chicken * 2 + rabbit * 4 == leg:
        print("鸡",chicken, '兔', rabbit)
#

# h = 1
#
# def func():
#     print("func")
#     t = 3
#     def func1():
#         print("func1")
#         f = 2


# print(globals())
# print(locals())
# c = "123"
# print(type(c))


# book1 = ['红楼梦', '曹雪芹']
# book2 = ['西游记', '吴承恩']
# book3 = ['三国演义', '罗贯中']
# book4 = ['水浒传', '施耐庵']
# books = [book1, book2, book3, book4]
# print("-----------文学知识调查问卷-------------------")
# print("总共四题，每题25分")
# i = 0
# score = 0
# while i < 4:
#     a = input(books[i][0] + "的作者是：")
#     if a == books[i][1]:
#         score += 25
#         i += 1
#     else:
#         i += 1
# print("你的得分是", score)


# x = 'abc'
# print(x[0],x[1],x[2])

# msg='my name is sean'
# print(msg.__len__())

















# apple = 1
#
# _apple = 2
#
# apple_1 = 4

# apple = 5

# Frist = 10
#
# print(Frist)






