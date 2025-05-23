answer = input("Is today a good day? (y/n): ")

if answer.lower() == "y":
    for _ in range(10):
        print("Yes it is")



from colorama import init, Fore

init()

weather = input("What's the weather like today? ")

if weather == "Hot":
    print(Fore.RED + "It's really hot today!")
elif weather == "Cold":
    print(Fore.CYAN + "It's pretty cold out there.")
elif weather == "Windy":
    print(Fore.YELLOW + "It's super windy today.")
elif weather == "Balmy":
    print(Fore.GREEN + "Nice and balmy weather today.")
else:
    print("I don't know that weather type.")

