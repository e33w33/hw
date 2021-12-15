class Contact:

    def __init__(self, id, name, surname, birth, profession):
        self.id = id
        self.name = name
        self.surname = surname
        self.birth = birth
        self.profession = profession

    def __str__(self):
        return f' id - {self.id},' \
               f' name - {self.name},' \
               f' surname - {self.surname},' \
               f' birth - {self.birth}'\
               f' profession - {self.profession}'


contact1 = Contact(3033 ,'Melisa', 'Slaviskyte', '21.06.1999', 'Python Developer')
print(contact1)