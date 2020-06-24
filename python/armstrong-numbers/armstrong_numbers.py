import math
def is_armstrong_number(number):
    sum = 0
    number = str(number)
    power = len(number)
    for i in number:
        sum += math.pow(int(i), power)
    return number == sum

num = input("Pick a number: ")
print(is_armstrong_number(num))