def bubblesort(arr):
    """
    Sorts an array using the bubble sort algorithm.

    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr

arr=list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
sorted_arr = bubblesort(arr)
print("Sorted array:", sorted_arr)
# Output: Sorted array: [1, 2, 3, 4, 5]