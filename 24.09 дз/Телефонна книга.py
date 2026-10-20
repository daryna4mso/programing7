contacts = {}

while True:
    command = input("Введіть команду: ")

    if command == "add":
        name = input("Ім'я: ")
        number = input("Номер: ")
        contacts[name] = number

    elif command == "delete":
        name = input("Ім'я: ")
        if name in contacts:
            del contacts[name]

    elif command == "search":
        name = input("Ім'я: ")
        print(contacts.get(name, "Not found"))

    elif command == "show":
        for k, v in contacts.items():
            print(k, v)

    elif command == "exit":
        break