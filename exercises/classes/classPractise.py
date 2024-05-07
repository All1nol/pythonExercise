class Person:
    def __init__(self, Name, Surname, Age):
        self.Name= Name
        self.Surname= Surname
        self.Age = Age
    def print_Person(self):
        print("Person's Name os {}, Surname is {} and age is {}".format(self.Name,self.Surname, self.Age))
    def  is_adult(self):
        if self.Age>= 18:
            print("it is adult")
        else:
            print("it is teenager")

first_person = Person("Omar", "Mamedov", 19)
first_person.print_Person()
first_person.is_adult()
