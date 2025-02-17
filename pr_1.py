import datetime

class Anzhelika:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None

        current_year = datetime.datetime.now().year
        age = current_year - self.birth_year

        if age < 17:
            return "1 курс"
        elif age < 18:
            return "2 курс"
        elif age < 19:
            return "3 курс"
        else:
            return "Курс для людей іншого віку"

    def create_name_list(self):
        if self.name is None or self.surname is None:
            return []
        return [self.name, self.surname]

person1 = Anzhelika("Анжеліка", "Поручнік", 2007)

person2 = Anzhelika()

print(person1.calculate_course())
print(person1.create_name_list())

print(person2.calculate_course())
print(person2.create_name_list())