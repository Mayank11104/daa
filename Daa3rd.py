
def fractional_knapsack():

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
            items.append((ratio, value, weight, i + 1))

        if valid:
            capacity = int(input("Enter knapsack capacity: "))

            if capacity < 0:
                print("Capacity cannot be negative.")
            else:
                items.sort(key=lambda item: item[0], reverse=True)

                print("\nItems Sorted by Value/Weight Ratio:")
                for ratio, value, weight, item_no in items:
                    print("Item:", item_no,
                          "| Value:", value,
                          "| Weight:", weight,
                          "| Ratio:", round(ratio, 2))

                total_value = 0
                selected_weight = 0

                print("\nSelected Items in Knapsack:")

                for ratio, value, weight, item_no in items:

                    if capacity == 0:
                        break

                    if weight <= capacity:
                        capacity -= weight
                        total_value += value
                        selected_weight += weight

                        print("Item:", item_no,
                              "| Fully Selected",
                              "| Weight:", weight,
                              "| Value:", value)

                    else:
                        fraction = capacity / weight
                        used_weight = capacity
                        added_value = value * fraction

                        total_value += added_value
                        selected_weight += used_weight

                        print("Item:", item_no,
                              "| Partially Selected",
                              "| Weight:", used_weight,
                              "| Value:", round(added_value, 2))

                        capacity = 0

                print("\nTotal Weight Selected:", selected_weight)
                print("Maximum Value:", round(total_value, 2))


def main():

    while True:
        print("\nFRACTIONAL KNAPSACK")
        print("1. Solve Fractional Knapsack")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            fractional_knapsack()

        elif choice == 2:
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please select 1 or 2.")


main()
