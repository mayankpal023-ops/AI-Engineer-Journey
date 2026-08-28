class Student:
    # def hello():
    #     print("hello from student class") #this will give error because we are not passing self as parameter in the method
    @staticmethod # decorator
    def hello():
        print("hello from student class")

s1 = Student()
s1.hello()       