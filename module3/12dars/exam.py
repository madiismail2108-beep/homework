import json

class Card:
    def __init__(self,seria, pin, account):
        self.seria = seria 
        self.__pin = str(pin)
        self.account = account

    @property
    def pin(self):
        return self.__pin
    
    def check_pin(self,pin):
        return self.__pin == str(pin)

    
class User:
    def __init__(self,name):
        self.name = name
        self.cards : list[Card] = []

    def add_card(self, ncard):
        self.cards.append(ncard)
        
class Account:
    def __init__(self,owner : User,balance):
        self.owner = owner
        self.__balance = balance
        
    
    def deposit(self,amount): 
         self.__balance +=amount
    
    def withdraw(self,amount):
           if amount <= self.__balance:
               self.__balance -= amount
               return True
           return False
    
    def get_balance(self):
        return self.__balance
    
class Atm:
    def __init__(self,users):
        self.users = users
        self.current_user = None
        self.current_card = None

    def loggin(self):
         username = input("Enter username: ")
         pin = input("Enter PIN: ")
         for user in self.users:
            if user.name == username:
                for card in user.cards:
                    if card.check_pin(pin):
                        self.current_user = user
                        self.current_card = card
                        print(f"Welcome, {username}!")
                        return True
            print("Login failed.")
            return False
         
    def logout(self):
        print(f'Goodbye Mr|Ms {self.current_user.name}')
        self.current_user = None
        self.current_card = None

    def run(self):
        while True:
           if not self.current_user:
                if not self.loggin():
                    continue
           print("Choose what you want to do: ")
           print("1.Check balance")
           print("2.Top up balance ")
           print("3. Get money from card") 
           print('4. I am done')

           choice = int(input('Your choise: '))

           if choice == 1:
              print(f'Your balance {self.current_card.account.get_balance()}')

           elif choice == 2:
              amount = int(input("Enter amount to deposit: "))
              self.current_card.account.deposit(amount)
              print("Deposit successful!")

           elif choice == 3:
              amount = int(input("Enter amount to withdraw: "))
              if self.current_card.account.withdraw(amount):
                  print('Your withdraw is successful')
              print("You do not have enough money")
    
           elif choice == 4:
              self.logout()
           else:
               print('this is invalide choice! please choose another :)')

u1 = User("Alice")
acc1 = Account(u1, 1000)
card1 = Card("8600 1234 5678 9012", "1234", acc1)  
u1.add_card(card1)

atm = Atm([u1])
atm.run()
    

'''

1) login (username and pin)
2) get balance
3) deposit
4) widthdraw
4) logout

'''