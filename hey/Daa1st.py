#non recur
n = int(input("Enter number of terms for Non-Recursive: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Non-Recursive Fibonacci Series:")

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

#recur
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = int(input("\n\nEnter number of terms for Recursive: "))

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Recursive Fibonacci Series:")

    for i in range(n):
        print(fibonacci(i), end=" ")