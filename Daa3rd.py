
print("Fractional Knapsack using Greedy Method")

n = int(input("Enter number of items: "))

if n <= 0:
    print("Number of items must be positive.")
else:
    items = []
    valid = True

    for i in range(n):
        value = int(input("Enter value of item " + str(i + 1) + ": "))
        weight = int(input("Enter weight of item " + str(i + 1) + ": "))

        if value < 0 or weight <= 0:
            print("Value must be non-negative and weight must be positive.")
            valid = False
            break

        ratio = value / weight
        items.append((ratio, value, weight))

    if valid:
        capacity = int(input("Enter knapsack capacity: "))

        if capacity < 0:
            print("Capacity cannot be negative.")
        else:
            # Sort by value/weight ratio in descending order
            items.sort(key=lambda item: item[0], reverse=True)

            total_value = 0

            for ratio, value, weight in items:
                if capacity == 0:
                    break

                if weight <= capacity:
                    capacity -= weight
                    total_value += value
                else:
                    fraction = capacity / weight
                    total_value += value * fraction
                    capacity = 0

            print("Maximum value =", total_value)
