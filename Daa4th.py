
print("0/1 Knapsack using Dynamic Programming")

n = int(input("Enter number of items: "))

if n <= 0:
    print("Number of items must be positive.")
else:
    values = []
    weights = []
    valid = True

    for i in range(n):
        value = int(input("Enter value of item " + str(i + 1) + ": "))
        weight = int(input("Enter weight of item " + str(i + 1) + ": "))

        if value < 0 or weight <= 0:
            print("Value must be non-negative and weight must be positive.")
            valid = False
            break

        values.append(value)
        weights.append(weight)

    if valid:
        capacity = int(input("Enter knapsack capacity: "))

        if capacity < 0:
            print("Capacity cannot be negative.")
        else:
            # Create DP table
            dp = [[0 for _ in range(capacity + 1)]
                  for _ in range(n + 1)]

            # Fill the DP table
            for i in range(1, n + 1):
                for w in range(1, capacity + 1):
                    if weights[i - 1] <= w:
                        dp[i][w] = max(
                            values[i - 1] +
                            dp[i - 1][w - weights[i - 1]],
                            dp[i - 1][w]
                        )
                    else:
                        dp[i][w] = dp[i - 1][w]

            print("Maximum value =", dp[n][capacity])
