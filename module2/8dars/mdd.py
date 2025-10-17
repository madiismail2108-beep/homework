#1)
# en_uz={
#  'juice' : 'sharbat',
#  'jam' : 'murabbo',
#  'candy' : 'shirinlik',
#  'fruits' : 'mevalar',
# 'apple' : 'olma',
#  'lime' : 'limon',
#  'banana' : 'banan',
#  'cherry' : 'olcha',
#  'ice' : 'muz',
#  'icecream' : 'muzqaymoq'
#}

#while True:
#  word=input('soz kiriting (exit dep yozsayz chiq ketadi): ')
#  if word.lower() == 'exit':
#    break
#  for key, value in en_uz.items():
#    if word == key:
#      print(value)
#      break
#    elif word == value:
#      print(key)
#      break
#  else:
#    print(f'bunaqa soz {word} mavjud emas')

#2)
#def unique_letter_count(word : input) ->str:
#    return set(word) , len(word)

#word=input('soz kiriting: ')
#print(unique_letter_count(word))
#3)
#def symmetric_difference(list1, list2):
#  return set(list1).symmetric_difference(set(list2))

#print(symmetric_difference([1, 2, 3], [3, 4, 5]))

#4)
#def is_empty_set(list):
#  return len(list) == 0

#print(is_empty_set([1,2]))

#5)
#def can_be_palindrome(word):
#  reversed_word = word[::-1]  
#  if word == reversed_word:
#    return True
#  else:
#    return False
    
#word = input('soz kiriting: ')
#print( can_be_palindrome(word))

#6)
#def count_unique_letters(words):
#  return len(set(words))

#words=input('yozing: ')
#print(count_unique_letters(words))

#7)
#def count_unique_elements(list):
#    return len(set(list))

#list=[1,1,2,3,3,4,5,5]
#print(count_unique_elements(list))
    