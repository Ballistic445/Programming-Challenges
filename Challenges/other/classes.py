class Student:
    
    def __init__(self, Name: str, Age: int, Subjects: list):
        self.name = Name
        self.age = Age
        self.subjects = Subjects
    
    def DisplaySubjects(self):
        print(f"{self.name}: {self.subjects}")
        
bob = Student("bob", "29", ["maths", "english"])
bill = Student("bill", "3", ["Further maths", "neuroscience", "English literature"])
print(bob)
print(bob.name)
print(bill.DisplaySubjects())