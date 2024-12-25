import random

def roll_dice():
    while True:
        print(f"You rolled a {random.randint(1, 6)}!")
        roll_again = input("Roll again? (yes/no): ").lower()
        if roll_again != 'yes':
            print("Goodbye!")
            break

roll_dice()
