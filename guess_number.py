import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess the number between 1 to {x}"))
        if guess<random_number:
            print("Sorry value is low,please enter the number again")
        elif guess>random_number:
            print("Sorry values is high,please enter the number again")
    print(f"Yaa you guessed the correct number{guess}")


guess(10)