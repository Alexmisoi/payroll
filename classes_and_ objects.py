# Terminologies
# a class is a group of related functions and variables
# oop programming attached to objects
# in python a function inside a class is called methods
# object - an instance of a class.
# a constructor - is simply a special method  that runs every time you instantiate

# def student -function
# class student - creating class
class Student:
    math = 0
    Geo = 0
    Kis = 0
    ssr = 0
    total_marks = 0
    average = 0.0
    grade = ""

    # a constructor
    def __init__(self,math,Geo,Kis,ssr):
        self.math = math
        self.ssr = ssr
        self.Geo = Geo
        self.Kis = Kis
        self.find_total()
        self.find_average()
        self.find_grade()

    def find_total(self):
        self.total_marks = self.math+ self.Kis + self.Geo + self.ssr

    def find_average(self):
        self.average = self.total_marks/5

    def find_grade(self):
        ave = self.average
        if ave >= 80 and ave<= 100:
            self.grade = "A"
        elif ave >=70:
            self.grade = "B"
        elif ave >= 60:
            self.grade = "C"
        elif ave >= 50:
            self.grade = "D"
        else:
            self.grade = "E"



Alex = Student(45,65,47,98)
roy = Student(56,67,87,76)
said = Student(65,77,66,98)

Alex.find_total()
Alex.find_grade()

print(Alex.grade)
print(roy.grade)
