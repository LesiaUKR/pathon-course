import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name and self.email == other.email and
                    self.phone == other.phone and self.favorite == other.favorite)
        return False


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        self.contacts = contacts if contacts is not None else []

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


# Приклад використання:
contacts = [
    Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
    Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file("user_class.dat")
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # True
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
