import random

def flip_a_coin():
    side = ["Head","Tails"]
    a = input("The side you picked: ")
    result = random.choice(side)
    print(f"You picked:{a}\nResult:{result}")
    if a==result:
        return print("You Won!") 
    else: return print("You Suck.")

flip_a_coin()