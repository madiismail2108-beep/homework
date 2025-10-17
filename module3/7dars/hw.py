from datetime import datetime
from pylibdmtx.pylibdmtx import encode 
from PIL import Image
import segno

class Students:
    students={}
    def __init__(self,name,month_day):
        self.name=name
        self.date_of_birth=month_day
        Students.students[self.name]=self.date_of_birth

    def __str__(self):
        return f'{self.name} : {self.date_of_birth}'
    
    def __getitem__(self):
        if self.name not in Students.students:
            return f'there no one with this {self.name}'
        return f'{self.name}:{self.date_of_birth}'
    
    def __len__(self):
        return len(Students.students)
    
    def __sub__(self):
        age = datetime - self.date_of_birth
        return f" {self.name}: {age}"
    
    def make_datamatrix(self, filename=None):
        data = f"Name: {self.name}\nBirth: {self.date_of_birth}"
        
        encoded = encode(data.encode("utf-8"))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)

        if filename is None:
            filename = f"{self.name}_datamatrix.png"
        img.save(filename)
        print(f"{self.name} uchun Data Matrix saqlandi: {filename}")

s1 = Students("Ali", "2005-03-14")
s2 = Students("Madina", "2007-07-22")

a1=segno.helpers.make_datamatrix(s1)
a1.save('ali_adatamatrix.png')



    
