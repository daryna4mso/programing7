password = input("Введіть пароль: ")

lower = False
upper = False
digit = False

for char in password:
    if char.islower():
        lower = True
    elif char.isupper():
        upper = True
    elif char.isdigit():
        digit = True

if lower and upper and digit:
    print("Password is secure.")
else:
    print("Password is unsafe!")