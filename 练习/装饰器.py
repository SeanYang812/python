
import time
from functools import wraps






# start_time = time.time()
# timmer()
# end_time = time.time()
# print(end_time-start_time)
# def wrapper():
#     start_time = time.time()
#     res = timmer()
#     end_time = time.time()
#     print('运行时间：',end_time-start_time)
#     return res
#
# wrapper()
# def timmer_out(flag):
#     def timmer(func):
#         @wraps(func)
#         def wrapper():
#             if flag:
#                 start_time = time.time()
#                 res = func()
#                 end_time = time.time()
#                 print('运行时间：',end_time-start_time)
#                 return res
#             else:
#                 res = func()
#                 return res
#         return wrapper
#     return timmer
# @timmer_out(flag = True)
# def index():
#     """
#     打印hello Python
#     :return:
#     """
#     time.sleep(1)
#     print("hello python")
#
#
# print(index.__doc__)
# print(foo(index))
# foo(index)()
# index = foo(index)
# # print(foo()())
# index()

# def inner():
#     name = 'sean'
#     def wrapper():
#         print(name)
#         print("hello python")
#     return wrapper()


# import time
#
# def timmer():
#     time.sleep(1)
#     print("hello python")
#
#
# def index():
#     def wrapper():
#         print("ok")
#     return wrapper


import time
from functools import wraps



def index(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("运行时间：", end_time - start_time)
        return res
    return wrapper

@index
def timmer(a,b,c):
    time.sleep(1)
    print("hello python",a,b,c)



# timmer = index(timmer)


# index(timmer)()
timmer(1,2,c=3)
