db={
    'hello# hi# howa# whats up': 'salom#nima gam#assalomualaykum',
    'money#cash#balance#buck':'pul#soqqa#acha#tanga'
}

def get_word_by_split(word : str,splitter = "#"):
 return word.split(splitter)

def menu():
 print("en_uz => 1")
 print("uz_en =>2")
 return input("...")

def swap(search, result, choice):
  if choice == "2":
       search , result = result , search
  return search , result

def run():
 while True:
      choice = menu()
      if choice not in ["1","2","q"]:
         print("invalid choice")
         continue
        
      elif choice == "q":
         break
        
      word = input("Enter your word : ")
        
      for search , result in db.items():
          search , result = swap(search,result,choice)
          keys = get_word_by_split(search)
          if word in keys:
             result =  get_word_by_split(result)
             print(result)
             break
      else:
         print(f"{word} not found")

if __name__ =='__main__':
    run()


