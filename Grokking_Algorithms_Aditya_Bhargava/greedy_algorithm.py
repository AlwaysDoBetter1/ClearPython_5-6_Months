'''
Greedy algorithm. Let's implement the greedy algorithm for the "Fractional Knapsack Problem", where given weights
and values of items, we need to maximize the total value in the knapsack without exceeding its capacity.
'''

def fractional_knapsack(weights, values, capacity):
    # Calculate the value-to-weight ratio for each item
    ratios = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    # Sort the items based on their value-to-weight ratio in descending order
    ratios.sort(reverse=True)

    total_value = 0  # Total value of items in the knapsack
    knapsack = []    # Items selected for the knapsack

    for ratio, weight, value in ratios:
        if capacity == 0:
            break
        # Take the whole item if it fits completely into the knapsack
        if weight <= capacity:
            total_value += value
            capacity -= weight
            knapsack.append((weight, value, 1))  # Fraction of item taken
        else:
            # Take the fraction of the item that fits into the knapsack
            fraction = capacity / weight
            total_value += fraction * value
            knapsack.append((weight, value, fraction))  # Fraction of item taken
            capacity = 0

    return total_value, knapsack

# Example usage:
weights = [10, 20, 30]   # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50            # Capacity of the knapsack
max_value, selected_items = fractional_knapsack(weights, values, capacity)
print("Maximum value in knapsack:", max_value)
print("Selected items:", selected_items)
