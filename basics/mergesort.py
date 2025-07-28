import ast  # To safely parse string input as a Python list

def debug_print(debug_msg=None, **kwargs):
    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


def mergesort(array):
    if len(array) <= 1:
        return array

    m = len(array) // 2

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    debug_print("Before merge", left=left, right=right)
    result = merge(left, right)
    debug_print("After merge", merged=result)
    return result


def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

    return merged


if __name__ == "__main__":
    input_str = input("Enter a list of numbers (e.g., [1, 3, 4, 3]): ")
    try:
        value_list = ast.literal_eval(input_str)  # Safely parse the input string as a list
        if not isinstance(value_list, list):
            raise ValueError("Input is not a list.")
        if not all(isinstance(x, int) for x in value_list):
            raise ValueError("List must contain only integers.")
    except Exception as e:
        print("Invalid input:", e)
        quit(1)

    sorted_list = mergesort(value_list)
    print("Sorted list:", sorted_list)
