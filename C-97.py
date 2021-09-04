import random 
import colorama
colorama.init()

theNumber = random.randint (1, 20)

lives = 5


while lives != 0:

    attempt = int(input(colorama.Fore.MAGENTA + "\n \n Guess a number from one to twenty:"))


    if attempt == theNumber:
        print(colorama.Fore.GREEN + "You got it! WOOOO")
        lives = 0
    elif attempt > theNumber:
        print(colorama.Fore.RED + "WRONG, too high. " + str(lives) + " lives left \n")
        lives -= 1
    elif attempt < theNumber:
        print(colorama.Fore.RED + "WRONG, too low. " + str(lives) + " lives left \n")
        lives -= 1