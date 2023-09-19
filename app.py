def binary_search(list, element):
    # middle = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while start <= end:
        print("Steps", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start+end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
target = 3

# binary_search(my_list, target)

result = binary_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
