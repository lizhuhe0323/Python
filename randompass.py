import random

all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCEEFGHIJKLMNOPQRSTUVWXYZ"

num = int(input("Please input number of words:"))

def gen_pass(num=8):
    pwd = ""

    for i in range(num):
        ch = random.choice(all_chars)
        pwd += ch

    return pwd

if __name__ == '__main__':
    print(gen_pass(num))
    print(gen_pass())