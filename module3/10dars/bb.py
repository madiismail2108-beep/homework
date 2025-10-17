class CARD:
    def __init__(self, seria, owner, balance, password, phone_number=None):
        self.s = seria
        self.o = owner
        self.b = balance
        self.p = password
        self.ph=phone_number

    def __str__(self):
        return F"owner:{self.o}, his phone number:{self.ph}"


c1 = CARD(1234, 'monu', 12000000, 3333)
c2 = CARD(1224, 'millo', 22000000, 2222, 998771237777)

baza = (c1, c2)


def is_card(s: list):
    seria = input('Card seria: ')
    for item in s:
        if item.s == int(seria):  
            return item
    return False  
         
def Bancomat_manager(db:list):
    card=is_card(db)
    if card is None:
        return "This card not found"
    print(f"this card is found Owner:{card.o} His|Her phone number:{card.ph}")
    for i in range(3):
        password = input("CARD password: ")
        if card.p == int(password):
             print('password correct')
             break
        print('password correct')
    else:
       print('Too many atteps! Your card blocked!')

    while True:
        print("Choose what you want to do: ")
        print("1.Check balance")
        print("2.Top up balance ")
        print("3. Get money from card")
        print("4.Change card phone number") 
        print('5. I am done')

        choice = int(input('Your choise: '))

        if choice == 1:
          print(f'Your balance {card.b}')
        elif choice == 2:
          money = int(input("Amount of money that you want to put: "))
          card.b +=money
          print(f'Your actual balance: {card.b}')
        elif choice == 3:
          money = int(input("Amount of money that you want to get: "))
          if money > card.b:
             print('there not enough money')
          card.b -= money
          print(f'Get {money}')
        elif choice == 4:
          card.ph = int(input('New phone number: '))
        elif choice == 5:
           print('You are done')
           return
        else:
           print('invalid choice')
        
if __name__ =='__main__':
    Bancomat_manager(baza)
    

