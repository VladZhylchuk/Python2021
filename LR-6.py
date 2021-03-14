import random

def task1():
    user_score = random.randint(1,6)
    comp_score = random.randint(1,6)

    if user_score > comp_score:
        print(f"User won with score {user_score}:{comp_score}")
    else:
        print(f"Computer won with score {user_score}:{comp_score}")

def task2():
    user_score = 0
    comp_score = 0
    for i in range(2):
        user_score += random.randint(1, 6)
        comp_score += random.randint(1, 6)

    if user_score > comp_score:
        print(f"User won with score {user_score}:{comp_score}")
    elif user_score == comp_score:
        print(f"Draw score is {comp_score}:{user_score}")
    else:
        print(f"Computer won with score {comp_score}:{user_score}")

task2()