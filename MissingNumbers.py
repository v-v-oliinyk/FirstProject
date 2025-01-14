numbers1 = list(map(int, input("Please enter the sequence of numbers divided by comma: ").split(', ')))
numbers2 = []

# I wanted to create an "IF" for the input. but it makes an error automatically :D it's already enough.

def find_min_max(nums):
    return int(min(nums)), int(max(nums)) + 1

min_num, max_num = find_min_max(numbers1)

for number in range(min_num, max_num):
     numbers2.append(number)

numbers_diff = list(set(numbers2).difference(set(numbers1))) #found easily in Internet how to compare lists.

print(f"For '{numbers1}', the missing numbers are: '{numbers_diff}'")