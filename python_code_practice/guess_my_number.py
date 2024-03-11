import random

highscore=0
playagain="Y"
while playagain == "Y":
    secret_number = random.randint(1,20)
    score=20
    while True:
        guess = int(input("Enter number between 1 to 20:"))

        if guess == secret_number:
            print("Correct guess")
            if score > highscore:
                highscore = score
            print(f"Your score:{score}")
            print(f"High score:{highscore}")
            break
        elif guess > secret_number:
            score-=1
            print("Too high")
        else:
            score-=1
            print("Too low")

    playagain = input("Do you want to play again? press Y to play again, press N to exit the game:").upper()