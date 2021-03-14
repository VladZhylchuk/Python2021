import math


def task1():
    first_number  = int(input("first  number : "))
    second_number = int(input("second number : "))
    print(f"{first_number} + {second_number} =  {first_number + second_number}")
    print(f"{first_number} - {second_number} =  {first_number - second_number}")
    print(f"{first_number} * {second_number} =  {first_number * second_number}")
    print(f"{first_number} / {second_number} =  {first_number / second_number}")


def task2_1():
    x = int(input("Enter x : "))

    if 0 <= x < 2:
        y = x * math.sqrt(x - 5.4)
    elif 2 <= x < 8:
        y = math.atan(x**2)
    else:
        y = math.log2(x - 7.8)
    print(f"x = {x} y = {'% .2f' % y}")

def task2_2():
    natural_number = int(input("Enter natural number : "))
    is_odd    = natural_number % 2 == 1
    is_divide = natural_number % 5 == 0
    print(f"Natural number is odd  : {is_odd}")
    print(f"Natural number / 5 = 0 : {is_divide }")

def task2_3():
    liquid_volume   = int(input("Enter volume of liquid  : "))
    cube_side       = int(input("Enter size of the cube side : "))
    cylinder_height = int(input("Enter cylinder height :"))
    cylinder_radius = int(input("Enter cylinder radius :"))
    cube_volume     = cube_side ** 3
    cylinder_volume = cylinder_height * math.pi**2 * cylinder_radius

    fit_in_cube     = cube_volume     >= liquid_volume
    fit_in_cylinder = cylinder_volume >= liquid_volume

    if fit_in_cube  and fit_in_cylinder:
        print("Liquid  does fit in both containers")
    elif fit_in_cube:
        print("Liquid does fit in cube")
    elif fit_in_cylinder:
        print("Liquid does fit in cylinder")
    else:
        print("It`s too much liquid, it does not fit anything")
task2_3()

