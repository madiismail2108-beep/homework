class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __eq__(self,other):
        return (self.age == other.age) and (self.name == other.name)
    
    def __add__(self,other):
        return self.age + other.age
    
    def __gt__(self,other):
        return self.age > other.age

    def __ge__(self,other): 
        return self.age >= other.age
    
    def __str__(self):
        return self.name
    
    def __bool__(self):
        if self.age>=18:
            return True
        return False

    def __mult__(self,other):
        return self.age * other.age

    def __sub__(self,other):
        return (self.age - other.age) and (self.name-other.name)

    def __div__(self,other):
        if self.age>=other.age:
         return (self.age/other.age)
        return other.age / self.age
    

    