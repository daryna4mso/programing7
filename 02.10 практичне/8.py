import datetime

def is_adult(birth_year):
    current_year = datetime.datetime.now().year
    return current_year - birth_year >= 18