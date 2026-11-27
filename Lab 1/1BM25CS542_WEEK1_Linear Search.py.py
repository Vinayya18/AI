def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
            
    return -1  

numbers = [10, 50, 30, 70, 80, 20, 90, 40]
target_value = 30

result = linear_search(numbers, target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
