import random

def assign_moderator(user_list):
    return random.choice(user_list)

users = ["Олег", "Марія", "Іван"]
print(assign_moderator(users))