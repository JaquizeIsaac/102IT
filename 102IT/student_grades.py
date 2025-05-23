from colorama import init, Fore

init()

score = int(input("Enter points as a number between 0 and 100: "))

if score > 90:
    print(Fore.GREEN + "A")
elif score <= 90 and score > 80:
    print(Fore.BLUE + "B")
elif score <= 80 and score > 70:
    print(Fore.YELLOW + "C")
else:
    print(Fore.RED + "F")
