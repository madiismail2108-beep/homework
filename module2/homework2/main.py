#def biggest_number(a,b,c):
# return max(a,b,c)

#a = int(input("raqam kiriting: "))
#b = int(input("raqam kiriting: "))
#c = int(input("raqam kiriting: "))

#maximum = biggest_number(a,b,c)
#print("eng kotta raqam: ",maximum)

#def even_number(a):
  #  if a % 2 == 0:
   #     return "juft son"
  #  else:
#       return "toq son"

# result=even_number(a)
#print (result)

#def info(name, age):
 #   return 2025 - age

#name=input('ismingiz: ')
#age=int(input('yoshingiz: '))
#result=info(name, age)
#print(result)

#a = int(input("raqam kiriting: "))
#def square_and_cube(a):
#    square = a**2
#    cube = a**3
#    return f"kvadrat soni:{square}",f"kub soni:{cube}"

#result=square_and_cube(a)
#print(result)

a = int(input("raqam kiriting: "))
#b = int(input("raqam kiriting: "))
#def numbers(a,b):
    #if a<b:
    #    return f"{a} < {b} "
    #elif a>b:
    #    return f"{b} > {a} dan kotta"
    #else:
    #return f"{a} = {b} "

#result=numbers(a,b)
#print(result)

#def numbers(a,b):
 #   return f'{a}{b}{a}{b}'

#result=numbers(a,b)
#print(result)

def number(a):
    devisors=[]
    for i in range(1,11):
        if a % i == 0:
            devisors.append(i)
    return devisors 

result=number(a)
print('boluvchilari',result)