text = input()

letters = {}

for letter in text.lower():
    if letter.isalpha():
        letters[letter] = text.lower().count(letter)

most_common = max(letters, key=letters.get)

print(most_common.upper())