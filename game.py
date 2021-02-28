import random


available_options = ["rock", "paper", "scissors"]
users = {}


def get_option():
    random.seed()
    rand_int = random.randint(0, len(available_options) - 1)
    return available_options[rand_int]


def get_result(option1, option2):
    if option1 == option2:
        return "draw"
    res = available_options.index(option1) - available_options.index(option2)
    half = len(available_options) // 2
    if res < 0:
        res += len(available_options)
    if res <= half:
        return "win"
    if res > half:
        return "lose"


with open("rating.txt", "r") as users_file:
    for line in users_file:
        name, rating = line.split()
        users[name] = int(rating)
    user_name = input("Enter your name: ")
    print("Hello,", user_name)
    if not users.get(user_name):
        users[user_name] = 0
    options = input().split(",")
    if len(options) > 2 and len(options) % 2 == 1:
        available_options = options
    print("Okay, let's start")
    while True:
        my_turn = input()
        if my_turn == "!exit":
            print("Bye!")
            break
        if my_turn == "!rating":
            print("Your rating:", users[user_name])
            continue
        if my_turn not in available_options:
            print("Invalid input")
            continue
        comp_turn = get_option()
        battle_result = get_result(my_turn, comp_turn)
        if battle_result == "lose":
            print(f"Sorry, but the computer chose {comp_turn}")
        elif battle_result == "draw":
            users[user_name] += 50
            print(f"There is a draw ({comp_turn})")
        elif battle_result == "win":
            users[user_name] += 100
            print(f"Well done. The computer chose {comp_turn} and failed")
