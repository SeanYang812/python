# print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
num = [1,2,3,4,5,6,7,8,9]
inp = input("请输入数字1-9：").strip()
inp = int(inp)
if inp in num:
    for i in range(1, inp + 1):
        print("%s * %s = %-2s"%(inp, i, inp*i))
else:
    print("输入有误")



# -*- coding: utf-8 -*-
# import os
# from time import sleep
# repeat_times = 600
# def tap_screen(x, y):
#     os.system('adb shell input tap {} {}'.format(x, y))
#     if __name__ == '__main__':
#         for i in range(repeat_times):
#             if i > 0:
#                 tap_screen(2489, 1307)
#                 # 再次挑战
#                 print("再次挑战开始")
#                 sleep(5)
#                 tap_screen(2155, 1218)
#                 #闯关
#                 print("开始闯关")
#                 sleep(12)
#                 tap_screen(2764, 53)#自动
#                 print("自动按钮点击")
#                 sleep(50)
#                 tap_screen(500,500)#点击屏幕继续
#                 print("点击屏幕继续")
#                 sleep(5)
#                 tap_screen(2489, 1307) # 再次挑战
#                 sleep(1)
#                 print(i)