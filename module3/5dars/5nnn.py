#class Person:
  #  def __init__(self,first_name, last_name,age):
  #      self.first_name = first_name
  #      self.last_name = last_name
  #      self.age = age
  #     
  #  @property
 #  def full_name(self):
 #       return f'{self.first_name} {self.last_name}'
 #   
 #   @full_name.setter         
 #   def full_name(self, value):
 #       first, last = value.split(" ", 1)
 #       self.first_name = first
 #       self.last_name = last

 #   @full_name.deleter
 #   def full_name(self):
 #       print('delating full_name...')
 #       self.first_name=None
 #       self.last_name=None
    
 #    @property
  #   def age(self):         
  #      return self._age

   #  @age.setter
   #  def age(self, value):  
   #     if not isinstance(value, int):
   #         raise TypeError("Age must be in digit")
   #     if value < 0:
   #         raise ValueError("age must be natural number")
   #     self._age = value

    # @age.deleter
    # def age(self):        
    #    print("deleting age...")
    #   self._age = None

class Product:
    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount
        
    @property
    def discounted_price(self):
        if self.discount:
            total_price = self.price * (1- self.discount / 100)
            return total_price
        return self.price
        
    
    
    @property
    def self_name(self):
        return self.name
    
    @name.setter
    def name(self, value):        
        if not isinstance(value, str):
            raise TypeError("name of the product shoulbe in str")
        self._name = value

    @name.deleter
    def name(self):              
        print("Delating ...")
        self._name = None
