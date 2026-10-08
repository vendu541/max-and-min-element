def find_min_max(arr):
    largest = arr[0]
    smallest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest




n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

largest, smallest = find_min_max(arr)

print("Largest:", largest)
print("Smallest:", smallest)