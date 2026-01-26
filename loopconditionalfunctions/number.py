#number guessing game

secret = 6

guess = int(input("enter any integer: "))

if(guess > secret):
    print("Too high!")
elif(guess < secret):
    print("Too low!")
else:
    print("correct!")

