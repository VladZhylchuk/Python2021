def task1():
    sentence1 = "Hello, my name is Vlad"
    sentence2 = "My name is Vlad"
    print(f"Is any comae in sentence : {sentence1.find(',') != -1}")
    print(f"Is any comae in sentence : {sentence2.find(',') != -1}")


def task2():
    stroke = "abcdefghijklmnopqrstuvwxyz"
    print(f"Every odd item in srroke : {stroke[1:26:2]}")
    print(f"Reversed stroke : {stroke[::-1]}")
    print(f"Reversed stroke through one : {list(stroke[::-1])}")
    print(f"Length of stroke : {len(stroke)}")


def task3():
    a_stroke = input("a stroke : ")
    b_stroke = input("b stroke : ")
    c_stroke = input("c stroke : ")
    d_stroke = a_stroke + " " + b_stroke + " " + c_stroke + " "
    print(d_stroke )

task2()