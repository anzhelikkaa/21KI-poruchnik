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

class ExtendedAnzhelika(Anzhelika):
    def __init__(self, name=None, surname=None, birth_year=None, address=None, phone=None, email=None):
        super().__init__(name, surname, birth_year)
        self.address = address
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.surname}, {self.calculate_course()}, Address: {self.address}, Phone: {self.phone}, Email: {self.email}"

    def is_contact_info_complete(self):
        return all([self.address, self.phone, self.email])

    def _protected_method_example(self):
        # Приклад захищеного методу
        return f"Protected info: {self.name} {self.surname}"

person1 = ExtendedAnzhelika("Анжеліка", "Поручнік", 2007, "Макасіни 22А", "+380123456789", "anzhelika@gmail.com")
person2 = ExtendedAnzhelika()

print(person1)
print(person1.is_contact_info_complete())
print(person2)
print(person2.is_contact_info_complete())
print(person1._protected_method_example())
