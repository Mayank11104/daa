
def non_recursive(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def recursive(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

def main():
    while True:
        print("\n\nFIBONACCI SERIES")
        print("1. Non-Recursive")
        print("2. Recursive")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of terms: "))

            if n <= 0:
                print("Please enter a positive integer")
            else:
                print("Non-Recursive Fibonacci Series:")
                non_recursive(n)

        elif choice == 2:
            n = int(input("Enter number of terms: "))

            if n <= 0:
                print("Please enter a positive integer")
            else:
                print("Recursive Fibonacci Series:")
                recursive(n)

        elif choice == 3:
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")

main()