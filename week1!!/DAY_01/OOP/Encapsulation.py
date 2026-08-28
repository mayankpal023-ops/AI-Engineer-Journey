class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        return sum(self.marks)/len(self.marks)
s1 = Student("tony stark", [90, 80, 70])
print(s1.get_average())    
#encapsulation means wrapping up of data and methods into a single unit. In python we can achieve encapsulation by using private and protected access modifiers. A private member is accessible only within the class in which it is defined. A protected member is accessible within the class in which it is defined and also in its subclasses. In python we can make a member private by adding double underscore before its name and we can make a member protected by adding single underscore before its name.