import time
import matplotlib.pyplot as plt
from sys import maxsize 
from itertools import permutations

flag = False

def print_subset_sum(i, n, _set, target_sum, subset):
    global flag
    # If targetSum is zero, then there exists a subset
    if target_sum == 0:
        # Prints valid subset
        flag = True
        print("[", end=" ")
        for element in subset:
            print(element, end=" ")
        print("]", end=" ")
        return

    if i == n:
        # Return if we have reached the end of the array
        return

    # Not considering the current element
    print_subset_sum(i + 1, n, _set, target_sum, subset)

    # Consider the current element if it is less than or equal to targetSum
    if _set[i] <= target_sum:
        # Push the current element into the subset
        subset.append(_set[i])

        # Recursive call for considering the current element
        print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset)

        # Remove the last element after recursive call to restore subset's original configuration
        subset.pop()

def subset_sum_time(set_):
    global flag

    def print_subset_sum(i, n, _set, target_sum, subset):
        global flag

        if target_sum == 0:
            flag = True
            return

        if i == n:
            return

        print_subset_sum(i + 1, n, _set, target_sum, subset)

        if _set[i] <= target_sum:
            subset.append(_set[i])
            print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset)
            subset.pop()

    subset = []
    target_sum = sum(set_) // 2  # We're looking for subsets with a sum equal to half of the total sum
    start_time = time.time()
    print_subset_sum(0, len(set_), set_, target_sum, subset)
    end_time = time.time()

    return end_time - start_time

# Driver code
if __name__ == "__main__":
    # Test case 1
    set_1 = [1, 2, 1]
    sum_1 = 3
    n_1 = len(set_1)
    subset_1 = []
    print("Output 1:")
    print_subset_sum(0, n_1, set_1, sum_1, subset_1)
    print()
    flag = False

    # Test case 2
    set_2 = [3, 34, 4, 12, 5, 2]
    sum_2 = 30
    n_2 = len(set_2)
    subset_2 = []
    print("Output 2:")
    print_subset_sum(0, n_2, set_2, sum_2, subset_2)
    if not flag:
        print("There is no such subset")
    
    num_cities_list = [4, 5, 6, 7, 8]  # Example: Test cities from 4 to 8
    time_spent_list = []

    for num_cities in num_cities_list:
        set_ = list(range(1, num_cities + 1))
        time_spent = subset_sum_time(set_)
        time_spent_list.append(time_spent)

    # Plotting
    plt.plot(num_cities_list, time_spent_list, marker='o', color='b')
    plt.title('Time Spent by Algorithm vs. Number of Cities')
    plt.xlabel('Number of Cities')
    plt.ylabel('Time Spent (s)')
    plt.grid(True)
    plt.show()
