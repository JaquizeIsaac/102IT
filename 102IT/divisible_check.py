def is_divisible(number, divisor):
    return number % divisor == 0

number = int(input("What is the number: "))
divisor = int(input("What is the divisor: "))

if is_divisible(number, divisor):
    print(f"{number} is divisible by {divisor}")
else:
    print(f"{number} is NOT divisible by {divisor}")
