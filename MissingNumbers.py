from math import trunc

list3 = []

def find_min_max(number):
    return min(number), max(number)

def input_nums_sequence():
    list2 = []
    while True:
        list1 = input("Please enter a sequence of numbers separated by comma: ").split(",")

        if len(list1) <= 1:
            print("Please enter a valid SEQUENCE of numbers.")
            continue

        for num in list1:
            num = make_int(num)
            if not num:
                continue
            list2.append(num)  # it checks automatically when int() is not possible
        return list2

def make_int(string):
    try:
        return int(string.strip())
    except ValueError:
        print(f"Expected number. Got {string}.")

list2 = input_nums_sequence()

while True:
    pointer = input(f"Would you like to find missing numbers in any special range (0 - no, 1 - yes)?\n")
    if pointer == "1":
        minimal = make_int(input("Please enter the minimal number in range: "))
        maximal = make_int(input("Please enter the maximal number in range: "))
        if not minimal or not maximal:
            continue
    elif pointer == "0":
        minimal, maximal = find_min_max(list2)
    else :
        print("Please enter a valid answer.")
        continue

    full_range = range(minimal, maximal + 1)
    missing_numbers = sorted(set(full_range) - set(list2))

    if missing_numbers:
        print(f"Missing numbers in the sequence: {missing_numbers}")
    else:
        print("All numbers are present in the sequence.")
    break



