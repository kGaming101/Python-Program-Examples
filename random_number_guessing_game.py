import random

low = int(input("What should the lowest number be : "))
high = int(input("What should the highest number be : "))

guesses = 1

if low < high:
    picked = random.randint(low,high)
    print("The computer has picked a number from the range",low,"-",high)
    guess = ""
    while guess != picked:
        guess = int(input("Guess the number : "))
        if guess == picked:
            break
        if low > guess:
            print("Your guess was out of range. Now i'm sad. Goodbye.")
            break
        if high < guess:
            print("Your guess was out of range. Now i'm sad. Goodbye.")
            break
        guesses += 1
    print(picked,"was correct. It took you",guesses,"to guess the number correctly.")
else:
    print("Sorry, but",low,"is bigger than",high)