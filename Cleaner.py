skip_words = {"well", "kinda", "like", "uh", "and", "but", "it's"}
skip_symbols = {",", ".", ":", "!", "-"}
input_words = input("Tell me something: ").lower().split()
for word in input_words:
    if word in skip_words:
        input_words.remove(word)
    if word[-1] in skip_symbols:
        input_words.append(word[:-1].lower())
        input_words.remove(word) #Here word appends to the end of list, but in this example it doesn't matter.
sorted_list = sorted(input_words)
for idx, word in enumerate(sorted_list):
    print(f"- {word}")
# Well, i kinda think that you said.