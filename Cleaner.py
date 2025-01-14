skip_words = {"well", "kinda", "like", "uh", "and", "but", "it's"}
skip_symbols = {",", ".", ":", "!", "-"}
input_words = input("Tell me something: ").split()
for word in input_words:
    if word.lower() in skip_words:
        input_words.remove(word)
    if word[-1] in skip_symbols:
        input_words.append(word[:-1].lower())
        input_words.remove(word) #Here word appends to the end of list, but in this example it doesn't matter.

print(f"Meaningful words :{input_words}")
# Well, i kinda think that you said.