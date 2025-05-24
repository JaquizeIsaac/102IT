name = input("What is your name: ")
color = input("What is your favorite color: ")
friend = input("What is one of your friend's names: ")
vehicle = input("What is your favorite vehicle brand: ")
school = input("What elementary school did you attend: ")

with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Color: {color}\n")
    file.write(f"Friend's Name: {friend}\n")
    file.write(f"Favorite Vehicle Brand: {vehicle}\n")
    file.write(f"Elementary School: {school}\n")
