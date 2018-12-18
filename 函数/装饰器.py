import time


def index():
    time.sleep(1)
    print("hello python")
    return 122

def timmer(func):
    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        total_time = time.time() - start_time
        print(total_time)
        return res
    return wrapper

index = timmer(index)

index()
# print(a)