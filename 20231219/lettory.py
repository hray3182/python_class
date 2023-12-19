import random

def lettory():
    # 用 sample 生成不重覆數字
    lettory = random.sample(range(1, 46), 6) 
    lettory.sort()
    return lettory

if __name__ == '__main__':
    print(lettory())