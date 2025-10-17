#fruits=['apple','watermelon','banana']
#def get_all_fruits():
 #for counter , fruit in enumerate(fruits,1):
 #  print(counter,fruit)


#def create_fruit(fruit):
  #if not isinstance(fruit,str):
   #   return 'fruit not avaliable'
  #if fruit in fruits:
   #     return 'fruit is  avaliable'
  #fruits.append(fruit)
 # return 'fruit successfully added'


#def get_fruit(index):
#    if 1 <= index <= len(fruits):
  #   return fruits(index - 1)
 #   return 'fruit cannot founded'

#def update_fruit(index, new_fruits):
 #   if 1< index > len(fruits):
 #     return 'fruit not avaliable'
#    fruits[index-1] == new_fruits
 #   return 'fruit successfulle updated'


#def delate_fruit(index):
#    if 1 <= index <= len(fruits):
#      fruits.pop(index-1)
#      return 'fruit delated'
#    return 'fruit not founded'

#def menu():
 #  print('get_all_fruits => 1')
  # print('create_fruit   => 2')
  # print('get_fruit      => 3')
  # print('update_fruit   => 4')
   #print('delate_fruit   => 5')
   #print('exit           => ex')
#   return input('choice:')

#def run():
#    while True:
#      choice = menu()
#      if choice == '1':
#             get_all_fruits()
#      if choice == '2':
#             new_fruit=input('enter fruit name: ')
#             result=create_fruit(new_fruit)
  #           print(result)
  #    if choice == '3':
    #         index=int(input('index=> '))
   #          result= get_fruit(index)
  #           print(result)
  #    if choice == '4':
 #           get_all_fruits()
#            index=int(input('index=> '))
#            result= update_fruit(index)
#            print(result)
#      if choice == '5': 
#            get_all_fruits()
#            index=int(input('index=> '))
#            result= delate_fruit(index)
#            print(result)
#      if choice == 'ex':
#          return
          

#if __name__ == '__main__':
#    run()

def reversed_string(st):
  if len(st) <=1:
    return st
  return reversed_string(st[1:]) + st[0]

text=input('add word: ')
reversed_text=reversed_string(text)
print(reversed_text)
    