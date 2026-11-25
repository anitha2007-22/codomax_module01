terms = int(input("How many terms? "))

if terms < 0:
    print("Please enter zero or a positive number.")
else:
    first, second = 0, 1

    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second

    print()