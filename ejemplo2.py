"""find vowels in a word"""
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Palabra: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print("vocales: ", found)