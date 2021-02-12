import random
# range
print("Select the range")
minimum = int(input("Enter the minimum number"))
maximum = int(input("Enter the maximum number"))
a = random.randint(minimum,maximum)
trialsPlayer1 = 0
while  True:
    print("PLAYER 1 CHANCE!!!")
    guess = int(input(f"Guess the number between {minimum} to {maximum}\n"))
    trialsPlayer1 = trialsPlayer1 + 1
    if guess==a:
        print("You guessed it right!!!")
        print(f"Trials required to guess = {trialsPlayer1}")
        break
    elif guess>a:
        print("You guessed Wrong")
        print("guess a number little lesser")
        continue
    elif guess<a:
        print("You guessed Wrong")
        print("guess a number little greater")
        continue
print("Select the range")
minimumPlayer2 = int(input("Enter the minimum number"))
maximumPlayer2 = int(input("Enter the maximum number"))
aa = random.randint(minimumPlayer2,maximumPlayer2)
trialsPlayer2 = 0
while  True:
    print("PLAYER 2 CHANCE!!!")
    guess = int(input(f"Guess the number between {minimumPlayer2} to {maximumPlayer2}\n"))
    trialsPlayer2 = trialsPlayer2 + 1
    if guess==aa:
        print("You guessed it right!!!")
        print(f"Trials required to guess = {trialsPlayer2}")
        break
    elif guess>aa:
        print("You guessed Wrong")
        print("guess a number little lesser")
        continue
    elif guess<aa:
        print("You guessed Wrong")
        print("guess a number little greater")
        continue

if trialsPlayer2==trialsPlayer1:
    print("ITS A DRAW!!!")
elif trialsPlayer2>trialsPlayer1:
    print("PLAYER2 WON!!!")
elif trialsPlayer2<trialsPlayer2:
    print("PLAYER1 WON!!!")


