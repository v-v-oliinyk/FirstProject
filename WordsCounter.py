string_input = input("Enter the string of words: ")
string_dict = {}
for word in string_input.lower().split():
    if word in string_dict:
        string_dict[word] += 1
    else:
        string_dict[word] = 1
print(string_dict)