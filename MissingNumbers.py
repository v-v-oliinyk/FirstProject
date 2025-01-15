# numbers1 = list(map(int, input("Please enter the sequence of numbers divided by comma: ").split(', ')))
numbers1 = list(input("Please enter the sequence of numbers divided by comma: ").split(', '))
numbers2 = []

# I wanted to create an "IF" for the input. but it makes an error automatically :D it's already enough.
if not numbers1 or len(numbers1) == 1:
    print("Please try again.")
    exit()

def find_min_max(nums):
    return int(min(nums)), int(max(nums))

min_num, max_num = find_min_max(numbers1)

for number in range(min_num, max_num + 1):
     numbers2.append(str(number))

numbers_diff = set(numbers2).difference(set(numbers1)) #found easily in Internet how to compare lists.

for number in numbers_diff:
    numbers_diff.remove(number)
    numbers_diff.add(int(number))


print(f"For '{numbers1}', the missing numbers are: '{sorted(numbers_diff)}'")
