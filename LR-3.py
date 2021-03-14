import math


def task1():
    x = 0.1
    while x < 1.2:
        y = math.tan(0.5 * x) / (x**3 + 7.5)
        print(f"x :{'% .2f' % x}  y :{'% .3f' % y}")
        x += 0.1

def task2():
    x = 0.5
    while x < 0.9:
        y = math.tan(0.5 * x) / (x**3 + 7.5)
        print(f"x :{'% .2f' % x}  y :{'% .3f' % y}")
        x += 0.05

def task3():
    try:
        number_of_values = int(input("Enter number of values you need : "))
        print("Pound  Kilo")
        for i in range(1, number_of_values+1):
            print(f"{i}     {'% .3f' % (i * 0.453)}")

    except ValueError:
        print("Enter a number ")
        task3()
