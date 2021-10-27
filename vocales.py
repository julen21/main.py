

vowels = ["a", "e", "i", "o", "u"]
word = input("Introduce la palabra: ")
v_freg = {"a":0, "e":0, "i":0, "o":0, "u":0}
for letter in word:
    if letter in vowels:
        v_freg[letter]  +=1
print(f"Frecuencia de las vocales en {word}:\n{v_freg}", word, v_freg)