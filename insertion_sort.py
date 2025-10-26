# insertion_sort.py
# Insertion Sort Algorithm - Monotonically Decreasing Order

def insertion_sort_desc(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
if __name__ == "__main__":
    # Example 1
    data = [9, 5, 1, 4, 3]
    print("Original array:", data)
    insertion_sort_desc(data)
    print("Sorted (descending):", data)

    # Example 2
    nums = [10, 2, 33, 5, 78, 1]
    insertion_sort_desc(nums)
    print("Sorted (descending):", nums)
