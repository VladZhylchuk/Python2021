# Ввести з клавіатури натуральне число (не менше 5 цифр).
# Вивести на екран всі цифри заданого числа в стовпчик
#  по одній, починаючи з першої

def task1():
    user_big_number = int(input("Enter big number : "))
    scatter_number = []


    while user_big_number:
        scatter_number.append(user_big_number % 10)
        user_big_number //= 10

    for num in scatter_number[::-1]:
        print(num)

def task2():
    big_number = int(input("Enter big number : "))
    flag = 0
    while big_number:
        big_number_remnant = big_number % 10
        big_number //= 10
        if big_number_remnant == big_number % 10:
            flag = 1
            break
    if flag:
        print("Here is the same digits in a row")
    else:
        print("Here is no same digits in a row")



task2()
