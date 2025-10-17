#masala1
#number1=float(input('a= '))
#number2=float(input('b= '))
#result=number1 + number2
#print( 'c=' ,result)

#masala2
#number1=float(input('a= '))
#number2=float(input('b= '))
#number3=float(input('d='))
#result=(number1+number2+number3)/2
#print('c=', result)

#masala3
#number=float(input('a= '))
#result=(number)**2
#print('a^= ', result)

#masala4
#number1=float(input('a= '))
#number2=float(input('b= '))
#result=(number1)*(number2)
#print('c=',result)

#masala5
#number=float(input('a= '))

#if number>0:
 #print('sizning soningiz musbat')

#elif number<0:
 # print('sizni soninggiz musbat')

#else:
 # print('bu song nol')

#masala6
#number1=float(input('a= '))
#number2=float(input('b= '))
#number3=float(input('d='))

#if number1<number2<number3:
#print("d song eng kotta")

#elif number1>number2>number3:
  #  print("a song eng kotta")

#else:
   # print("b song eng kotta")

#masala7
#day_number = int(input("1 dan 7 gacha son kiriting: "))

#if day_number == 1:
  #  print("Bu - Dushanba")
#elif day_number == 2:
   # print("Bu - Seshanba")
#elif day_number == 3:
   # print("Bu - Chorshanba")
#elif day_number == 4:
  #  print("Bu - Payshanba")
#elif day_number == 5:
   # print("Bu - Juma")
#elif day_number == 6:
    #print("Bu - Shanba")
#elif day_number == 7:
   # print("Bu - Yakshanba")
#else:
    #print("Siz faqat 1 dan 7 gacha bo'lgan sonni kiritishingiz mumkin.")

#masala8
#year_number=int(input('hohlagan yilingizni kiriting: '))

#if year_number/4==0 or year_number/100==0 or year_number/400==0:
 #   print(' bu kabisa yil')
#else:
 #   print(' bu kabisa yil emas')

#masala9
#number=int(input('n= '))
#x=0
#for i in range(1, number+1):
 #   x+=i
 #   print('1 dan boshlab n gacha bolgan sonlar',number,'yegindisi bu ',x)
    
#masala10
#for i in range(10):
 #   print('Salom Dunyo')

#masala11
#i=1
#while i<=number:
 #   if number%i==0:
 #       print(i)
#i+=1

#masala12
result = 0

while True:
    number = input('Son yoki "exit" kiriting: ')
    
    if number.lower() == 'exit':
        break
    elif number.isdigit():
        result += int(number)
    else:
        print('Faqat son yoki "exit" kiriting!')
print(f'Result: {result}')
 
 


