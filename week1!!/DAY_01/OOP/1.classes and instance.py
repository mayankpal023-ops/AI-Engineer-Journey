# class Student:
#     name = "karan"

# s1 = Student()
# print(s1.name)    

# class car:
#     color = "blue"
#     brand = "bmw"

# car1 = car()
# print(car1.color)
# print(car1.brand)    

#constructor
# class Student:
#     clg = "abc college" #class variable
#     name = "anonymous" #class attribute
#     #default constructor
#     def __init__(self): # self is a reference variable which refers to the current object
#         pass

#     #parameterized constructor
#     def __init__(self, name,marks):
#         self.name = name # obj attribute > class attribute
#         self.marks = marks
#         print("adding new student in database..")

#     def welcome(self):
#         print("welcome to the class", self.name)    

#     def get_marks(self):
#         return self.marks    

# s1 = Student("karan", 90)
# print(s1.name, s1.marks)      

# s2 = Student("arjun", 88)
# print(s2.name, s2.marks)

# print(Student.clg)

# print(s1.name) #obj attribute
# s1.welcome()
# print(s1.get_marks())



class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        return sum(self.marks)/len(self.marks)    

s1 = Student("tony stark", [90, 80, 70])
print(s1.get_average())


s1.name = "iron man"
print(s1.name)