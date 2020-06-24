import math
def is_armstrong_number(number):
    sum = 0
    var = str(number)
    power = len(var)
    for i in var:
        sum += math.pow(int(i), power)
        print(sum)
    return number == sum

print("This is the armstrong numbers activity.")
#num = input('Pick a number: ')
print(is_armstrong_number(400))
print(is_armstrong_number(371))
