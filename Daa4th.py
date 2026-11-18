
def knapsack():

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

                # Backtracking to find selected items
                selected_items = []
                w = capacity

                for i in range(n, 0, -1):

                    if dp[i][w] != dp[i - 1][w]:
                        selected_items.append(i)
                        w -= weights[i - 1]

                selected_items.reverse()

                # Display selected items
                print("\nSelected Items in Knapsack:")

                total_weight = 0
                total_value = 0

                if not selected_items:
                    print("No items selected.")

                for item in selected_items:
                    index = item - 1

                    print("Item:", item,
                          "| Weight:", weights[index],
                          "| Value:", values[index])

                    total_weight += weights[index]
                    total_value += values[index]

                print("\nTotal Weight Selected:", total_weight)
                print("Total Value Selected:", total_value)
                print("Maximum value =", dp[n][capacity])


def main():

    while True:
        print("\n===== 0/1 KNAPSACK =====")
        print("1. Solve 0/1 Knapsack")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            knapsack()

        elif choice == 2:
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please select 1 or 2.")

 
main()
