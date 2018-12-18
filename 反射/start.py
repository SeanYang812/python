# import view
#
#
# def home():
#     print("网站首页")
#
# def run():
#     inp = input("请输入你想要访问的页面：").strip()
#     # 最初版:
#     # if inp == "login":
#     #     view.login()
#     # elif inp == "logout":
#     #     view.logout()
#     # elif inp == "index":
#     #     view.index()
#
#     # 简单版：
#     # func = getattr(view,inp)
#     # print(func)
#     # func()
#
#     # 改善版
#     # setattr(view,inp,home)
#     # delattr(view,inp)
#     if hasattr(view,inp):
#         func = getattr(view,inp)
#         func()
#     else:
#         print("404")
#
# if __name__ == '__main__':
#     run()


t = [1,2,3,3]

dic = {"l":1}
print(type(t))
print(type(dic))