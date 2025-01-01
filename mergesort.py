def merge_sort(array):
    if len(array) > 1:
        # Find the middle point
        m = len(array) // 2
        left = array[:m]
        right = array[m:]

        # Debug: Print the current array and midpoint
        print(f"array: {array}")
        print(f"m: {m}")

        # Recursively split and merge
        merge_sort(left)
        merge_sort(right)

        # Merging process
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        # Debug: Print merging details
        print("Merging...")
        print(f"left: {left}")
        print(f"right: {right}")
        print(f"merged: {array}")


# Input handling
input_list = input("Enter numbers, separated by ',': ").split(',')
value_list = [int(x.strip()) for x in input_list]
print(f"input_list: {input_list}")
print(f"value_list: {value_list}")

merge_sort(value_list)
print(value_list)
