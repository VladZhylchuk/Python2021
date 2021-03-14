# 1.	Дано натуральне число. Визначити, чи буде це число:
# непарн , кратним 5.
def task1():
    natural_number = int(input("Enter number : " ))

    if natural_number % 5 == 0:
        print("Number is multiple of 5")
    elif natural_number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    task1()


def task2():
    array_size = int(input("Enter size of array : "))
    array = [int(input(f"Enter {i+1} item : ")) for i in range(array_size)]

    summ = counter = 0

    for num in array:
        if num > 0:
            summ += num
            counter += 1
    print(f"sum {summ} count {counter}")




