name1 = input('name 1')
age1 = int(input('age1: '))


name2 = input('name 2')
age2 = int(input('age2: '))

if age1> age2:
    print(name1)
else:
    print(name2)




#for name, age in info.items():
#    if age >=15:
#      print( f'{name}')

#2)
#a=input('ismiz: ')
#b=int(input('tugilgan yiliz: '))
#if b % 4 ==0 or b % 100 ==0 or b % 400 ==0 :
#    print(f'{a} kabisa yilida tugilgan')
#else:
#    print(f'{a} kabisa yilida tugilmagan') 

#3)
#def number_in_words(n: int) -> str:
#    ones = ['nol', 'bir', 'ikki', 'uch', 'tort', 'besh', 'olti', 'yetti', 'sakkiz', 'toqqiz']
#    tens = ['on', 'yigirma', 'ottiz', 'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'toqson']
    
#    if 0 <= n < 10:
#        return ones[n]
#    elif 10 <= n < 20:
#        r = n % 10
#        if r == 0:
#            return 'on'
#        return f'on {ones[r]}'
#    elif 20 <= n < 100:
#        d = (n // 10) 
#        r = n % 10
#        if r == 0:
#            return tens[d - 1]
#        return f'{tens[d - 1]} {ones[r]}'
#    elif n == 100:
#        return 'yuz'
#    else:
#        return 'out of range'

#n = int(input('raqam: '))
#print(number_in_words(n))

#4)
#n = int(input('raqam kirit: '))
#l1 = []  
#l2 = []  
#l3 = [] 

#for i in range(1, n + 1): 
 #   if i <= 0:
 #       l3.append(i)
 #   elif i % 2 == 0:
 #       l2.append(i)
 #   else:
 #       l1.append(i)

#print("toq:", l1)
#print("juft:", l2)
#print("raqam:", l3)

#5)
#sozlar = []
#while True:
#    soz = input("So'z kiriting (chiqish uchun 'exit' deb yozing): ")
#    if soz.lower() == 'exit':
#        break
#    if soz not in sozlar:
#        sozlar.append(soz)

#print("Foydalanuvchi kiritgan so'zlar (taklarsiz):")
#for soz in sozlar:
#    print(soz)
    
#6)
#n = int(input("n = "))
#result = {x: x**2 for x in range(1, n+1)}
#print(result)

#7)
#users=[
#    {'username' : 'John',
#     'age' : 24,
#     'gender' : 'male'
#     },
#     {'username' : 'Ana',
#        'age' : 14,
#      'gender' : 'female'
#     },
#     {'username' : 'Mike',
#        'age' : 59,
#      'gender' : 'male'
#    },
#     {'username' : 'Monu',
#        'age' : 19,
#      'gender' : 'female'
#     },
#]


#filtered_users = [user for user in users if user['age'] > 18 and user['gender'].lower() == 'male']

#print("18 yoshdan katta erkak foydalanuvchilar:")
#for user in filtered_users:
#    print(f"{user['username']}, {user['age']}, {user['gender']}")