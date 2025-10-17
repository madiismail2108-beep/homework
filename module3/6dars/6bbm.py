class Product:
    def __init__(self, name, price, discount, code):
        self.name = name
        self.price = price
        self.discount = discount
        self.code = code

    
    @property
    def discounted_price(self):
        if self.discount:
            return self.price * (1 - self.discount/100) * 100
        return self.price

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):        
        if not isinstance(value, str):
            raise TypeError("name of the product should be str")
        self._name = value

    @name.deleter
    def name(self):              
        print("Deleting name ...")
        self._name = None

   
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value):
        if not isinstance(value, str):
            raise TypeError("code should be str")
        if len(value) < 4:
            raise ValueError("code must be at least 4 characters long")
        self._code = value

    @code.deleter
    def code(self):
        print("Deleting code ...")
        self._code = None
