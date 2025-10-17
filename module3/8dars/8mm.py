#1)single
#class group:
#   def a(self, name:str, group:int):
#        self.name=name
#        self.group_number=group

#class frds(group):
#    def b(self, id:str, date_of_birth:int):
#        self.id=id
#        self.date_of_birth=date_of_birth

#    def c(self):
#        self.name=input('yourname: ')
#        self.group_number=input('group number:')
#        self.id=input('your id')
#        self.date_of_birth=('your date of birth')
#        return f'{self.name}/n {self.id}/n'

#2)Multiple
#class family:
#    def members(self, grandad, dad, grandmom, mom, son, doughter):
#        self.m1=grandad
#        self.m2=dad
#        self.m3=grandmom
#        self.m4=mom
#        self.m5=son
#        self.m6=doughter

#class jobs(family):
#    def mj(self):
#        return f"{self.m1}->engineer; {self.m2}->manager; {self.m3}->teacher; {self.m4}->painter; {self.m5}, {self.m6}-> students"
    
#class students(jobs):
 #   def studing(self):
 #       return f'{self.m5} studing at school; {self.m6} studing at university and working at machine building'

#3)hierarchical
#class Animals:
#    def types(animal, bats, penguin):
#        animal.t1=bats
#        animal.t2=penguin

#class Mammals(Animals):
#    def milk(animal):
#        return f'{animal.t1} is mammal'

#class Birds(Animals):
#    def egg(animal):
#        return f"{animal.t2} is bird"

#4) multiple
#class school:
#    def teachers(self, math, literature, painting, coding):
#        self.t1=math
#        self.t2=literature
#        self.t3=painting
#        self.t4=coding

#class students(school):
#    def classes(self, a, b, c, d):
#        self.cl1=a
#        self.cl2=b
#        self.cl3=c
#        self.cl4=d

#class main(school, students):
#    def main_tch(self):
#        return f'{self.t1} main teacher for {self.cl1}, {self.t2} main teacher for {self.cl2}, {self.t3} main teacher for {self.cl3}, {self.t4} main teacher for {self.cl4}'
    
#5)hibrid 
class Employees:
    def emp(self, name, age, email):
        self.info1=name
        self.info2=age
        self.info3=email

class practice_time(Employees):
    def prt(self, experience):
        self.info4=experience

class type_of_work(Employees):
    def speciality(self, work):
        self.info5=work

class info(practice_time, type_of_work):
    def information(self):
        return 'this employee registrated successfully'