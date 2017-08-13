import random

notCorrect = True
randomNumber = random.randint(0, 10)

while notCorrect:
    message = ""
    invalidInput = True
    numberGuessString = input("Guess what the number is from 0 to 10: ")

    while invalidInput:
        if numberGuessString.isdigit():
          if int(numberGuessString) >= 0 or int(numberGuessString <= 10):
            invalidInput = False
          else:
            numberGuessString = input("Out of range or invalid input.  Please enter a valid input: ")
        else:
            numberGuessString = input("Out of range or invalid input.  Please enter a valid input: ")

    numberGuess = int(numberGuessString)

    if numberGuess > randomNumber:
        message = "Too high"
    elif numberGuess < randomNumber:
        message = "Too low"
    else:
        numberGuessString = input("Correct!  Do you want to play again?")
        if "Yes" in numberGuessString:
            randomNumber = random.randint(0, 10)
        elif "No" in numberGuessString:
            notCorrect = False
        else:
            numberGuessString = input("Please enter valid input")
            invalidInput = True
            while invalidInput:
                if "Yes" in numberGuessString or "yes" in numberGuessString:
                    randomNumber = random.randint(0, 10)
                    invalidInput = False
                elif "No" in numberGuessString or "no" in numberGuessString:
                    randomNumber = random.randint(0, 10)
                    invalidInput = False
                else:
                    numberGuessString = input("Please enter valid input")
    print(message)













