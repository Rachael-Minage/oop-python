class Student:

    school="AkiraChix"
    def __init__(self,firstname,lastname,age,country):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country


    def fullname(self):
        return f"Hello {self.firstname} {self.lastname} welcome to {self.school}, you are {self.age}years old and welcome to {self.country}" 


    def year_of_birth(self):
        year_of_birth=2022-self.age
        return f"Hello you were born in {year_of_birth}"

    def initials(self):
        return f"Hello your initials are {self.firstname[0]}{self.lastname[0]}"           