# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Last i elements are already sorted
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Swap if the element found is greater than the next element
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # Example usage
# if __name__ == "__main__":
#     numbers = [64, 34, 25, 12, 22, 11, 90]
#     print("Original list:", numbers)
#     bubble_sort(numbers)
#     print("Sorted list:", numbers)

# practice code from variables.py

def bubbleSort(arr):
    arrLen = len(arr)
    for i in range(arrLen):
        for j in range(0, arrLen - i - 1):
            print("Current array state:", arr)
            print(f"i={i}, j={j}")
            print(f"Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", numbers)
bubbleSort(numbers)
print("Sorted array is:", numbers)