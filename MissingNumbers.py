from math import trunc


def find_min_max(number):
    return min(number), max(number)

list2 = []
list3 = []

while True:
    try:
        list1 = input("Please enter a sequence of numbers separated by comma: ").split(",")
        for num in list1:
            num = num.strip()
            list2.append(int(num)) #it checks automatically when int() is not possible
        else:
            if len(list1) <= 1:
                print("Please enter a valid SEQUENCE of numbers.")
                continue

            while True:
                try:
                    pointer = input(f"Would you like to find missing numbers in any special range (0 - no, 1 - yes)?\n")
                    if pointer == "1":
                        min_spec_range = int(input("Please enter the minimal number in range: "))
                        max_spec_range = int(input("Please enter the maximal number in range: "))
                        full_range = range(min_spec_range, max_spec_range + 1)
                        missing_numbers = sorted(set(full_range) - set(list2))
                    elif pointer == "0":
                        minimal, maximal = find_min_max(list2)
                        full_range = range(minimal, maximal + 1)
                        missing_numbers = sorted(set(full_range) - set(list2))
                    else :
                        print("Please enter a valid answer.")
                        continue
                    if missing_numbers:
                        print(f"Missing numbers in the sequence: {missing_numbers}")
                    else:
                        print("All numbers are present in the sequence.")
                    break
                except ValueError:
                    print("Please enter a valid answer.")
            break
    except ValueError:
        print("An error occurred. Please enter a valid sequence of numbers.")


