#class Fib:
    #def __init__ (self,n):
    #    self.n=n
    #    self.a=0
    #    self.b=1
    #    self.index=0

    #def __iter__(self):
    #    return self
    
    #def __next__(self):
    #    if self.index>= self.n:
    #        raise StopIteration
    #    result = self.a
    #    self.a, self.b = self.b, self.a+self.b
    #    self.index+=1
    #    return result
    
def fib(n):
    a, b =0, 1
    for i in range(n):
        yield a
        a,b = b, a+b


n = int(input("Nechta Fibonacci sonini chiqaramiz? "))
#fib = Fib(n)

for num in fib(n):
    print(num)
