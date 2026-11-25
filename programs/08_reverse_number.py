a = int(input("Enter a non-negative integer: "))

if a < 0:
    print("Please enter a non-negative integer.")
else:
    reversed_number = 0

    while a > 0:
        digit = a % 10
        reversed_number = reversed_number * 10 + digit
        a //= 10

    print("Reversed number =", reversed_number)