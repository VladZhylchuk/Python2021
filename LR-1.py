def Task1():
    name = "Vladyslav"
    surname = "Zhylchuk"
    third_name = "Yuriiovych"
    print(f"Hello, {name} {surname} {third_name}")


def Task2():
    name = input("Enter your name : ")
    surname = input("Enter your surname : ")
    third_name = input("Enter your third_name : ")
    print(f"Hello, {name} {surname} {third_name}")


def Task3():
    room_length = int(input("Enter length of the room in cm : "))
    room_width = int(input("Enter width of the room in cm : "))
    print(f"Carpet you need is {room_length * room_width} square cm ")


def Task4():
    room_length = int(input("Enter length of the room in  cm : "))
    room_width = int(input("Enter width of the room in  cm : "))
    carpet_price = int(input("Enter price of your carpet per square mt : "))
    c_square = room_length * room_width
    m_square = room_length * room_width / 10000
    print(f"Carpet square is {c_square}  cm square")
    print(f"Carpet square is {m_square}  mt square")
    print(f"Actual price of the carpet is {carpet_price * m_square} ")


def Task5():
    result = 1
    for i in range(1, 21):
        result *= i
    print(result)


def Task6():
    print("A" * 100, sep=" ")


def Task7():
    print("Python" * 100)


def Task8():
    big_number = "179" * 50
    print(int(big_number) ** 2)


def Task9():
    name = input("Enter your name : ")
    print(f"Hello, {name}!")


def Task10():
    print(103, 25, 724, sep=", ")


def Task11():
    print('% .2f' % 156.12459835)


def Task12():
    print("     1.24     13.52" + "\n" +
          "    3.567   -355.1" + "\n" +
          "       8.2     9.18 ")


def Task13():
    print("{}, {}, {}".format(103, 25, 724))
    print('{:3.2f}'.format(156.12459835))
    print('{}\n{}\n{}'.format("     1.24     13.52",
                              "    3.567   -355.1",
                              "       8.2     9.18"))


def Task14_1():
    print("Numeric values")
    a = 1
    b = 2
    exp1 = a > b  # False
    exp2 = a < b  # True

    # not True  = False
    # not False = True

    print(exp1 and exp2)     # False and True = False
    print(not exp1 and exp2) # True  and True = True

    print(exp1 or not exp2)  # False or False = False
    print(exp1 or exp2)      # True  or False = True


    print("\nString values")
    a = 'a'
    b = 'b'
    # ord('a') = 97
    # ord('b') = 98
    exp2 = a < b  # True
    exp1 = a > b  # False

    print(exp1 and exp2)     # False and True = False
    print(not exp1 and exp2) # True  and True = True

    print(exp1 or not exp2)  # False or False = False
    print(exp1 or exp2)      # True  or False = True


def Task14_2():
    print("Hello, enter 2 numbers and check if 1 > 2")

    first_number  = int(input("Enter your first number : "))
    second_number = int(input("Enter your second number : "))
    print(f"{first_number} > {second_number} = {first_number > second_number}")
Task14_2()