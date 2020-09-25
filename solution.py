item1 = ['Sugar',  131,  50]
item2 = ['Bread(sliced)',  311,  200]
item3 = ['Bread(unsliced)',  229,  150]
item4 = ['Egg',  545,  50]
item5 = ['Three crown (tin)',  201,  150]
item6 = ['Peak milk (tin)',  230,  120]
item7 = ['Peak milk (sachet)',  791,  50]
item8 = ['Bournvita (sachet)',  611,  50]
item9 = ['Milo (tin)',  367,  500]
item10 = ['Peak milk (Large sachet)',  889,  700]
item11 = ['Milo (Large sachet)',  934,  700]
item12 = ['Bournvita (Large sachet)',  758,  100]
item13 = ['Custard (small sachet)',  383,  200]
item14 = ['Corn flakes (small sachet)',  647,  150]
item15 = ['Golden morn (small sachet)',  121,  100]
item16 = ['Detergent (small Wawu)',  198,  120]
item17 = ['Detergent (small Aerial)',  354,  115]
item18 = ['Detergent (Big Wawu)',  323,  200]
item19 = ['Detergent (Big Aerial)',  222,  250]
item20 = ['Corn flakes (Big sachet)',  341,  750]
item21 = ['Golden morn (Large sachet)',  458,  650]
item22 = ['Sprite (small)',  134,  80]
item23 = ['Pepsi (small)',  674,  80]
item24 = ['Fanta (small)',  757,  80]
item25 = ['Lacasera (small)',  127,  80]
item26 = ['Sprite (Big)',  956,  150]
item27 = ['Pepsi (Big)',  374,  150]
item28 = ['Fanta (Big)',  267,  150]
item29 = ['Lacasera (Big)',  786,  150]
item30 = ['Coke (Big)',  546,  150]

def Customer():
    print('Welcome, dear customer!')
    display_items()
    Stock()
    print('Thanks for placing your order')
    
    acces()

def display_items():
    print('-' * 50)
    print('Welcome')
    print('This is what we have in stock:')
    print('-' * 50)
    item = []
    item.append('s\n'  'item'  'Available Quantity'  'Price per quantity(N)')
    
    item.append(item1)
    item.append(item2)
    item.append(item3)
    item.append(item4)
    item.append(item5)
    item.append(item6)
    item.append(item7)
    item.append(item8)
    item.append(item9)
    item.append(item10)
    item.append(item11)
    item.append(item12)
    item.append(item13)
    item.append(item14)
    item.append(item15)
    item.append(item16)
    item.append(item17)
    item.append(item18)
    item.append(item19)
    item.append(item20)
    item.append(item21)
    item.append(item22)
    item.append(item23)
    item.append(item24)
    item.append(item25)
    item.append(item26)
    item.append(item27)
    item.append(item28)
    item.append(item29)
    item.append(item30)
    print(item)


def add_new_items():
    i=0
    item = []
    print("Do you want to add new item?: ")
    option = int(input('Choose option: \n 1. Yes \n 2. No '))
    if option == 1:
        while i <= 40:
            
            item_description = input("What item do you want to add: ")
            item[i] = item_description
            item_quantity = int(input("What quantity are you adding: "))
            item[i] = item_quantity
            item_price = int(input("How much will it cost: "))
            item[i] = item_price
            i += 1

    elif option == 2:
        Billing()

def Stock():
    
    prov_store =[]
    cosm_store =[]
    count=1
    a= input("Select Category: ")
    if (a == 'Provision'):
        d = input("Please Enter Today's date: ")
        z = int(input("How many items: "))
        while count <= z:
            print("Supply Item ", count)
            item = input("Item Name: ")
            quantity = int(input("Item quantity: "))
            prov_store = (d, 'SUPPLY', item, quantity)
            count = count+1
    else:
        print("Please enter correct category!")

def Billing():
    global receipt
    f = input("Please enter Today's date: ")
    K = input("Enter Transaction ID: ")
    z = int(input('Please Enter Number of Purchase items: '))
    count=1
    total=0
    Cash = []
    while count <= z:
        name = (input("Enter Product Description: "))
        quantity = int(input("Please Enter Purchase Quantity: "))
        unit_price = int(input("Enter unit price: "))
        total +=cost
        count +=1
        print("Total amount =", total, "Naira")
        if item <5:
            Discount= 0.2*total
            new_total= total-Discount
            Cash = (f, K, total, Discount, new_total)
            print('Discount =', Discount, 'Naira')
            print('Total Payment Due =', new_total, 'Naira')
        elif item >10:
            Discount= 0.3*total
            new_total= total-Discount
            Cash = (f, K, total, Discount, new_total)
            print('Discount =', Discount, 'Naira')
            print('Total Payment Due =', new_total, 'Naira')
        else:
            while item >10 and unit_price >100:
                new_total= total-800
                Cash = (f, K, total, Discount, new_total)
                print('Total Payment Due =', new_total, 'Naira')
                
        



def Admin():
    password = 'Admin'
    passcode = input('Enter password: ')
    if passcode == password:
        display_items()
        add_new_items()
        
    else:
        print("Sorry, you're not the admin")
        Billing()
        acces()

def Exit():
    print('Thank you')
    acces()

def main():
    acces()
    Admin()
    Customer()


def acces():
    access = int(input('Choose access: \n 1. Admin \n 2. User \n 3. Exit '))
    while access !=1 and access != 2 and access !=3:
        print('Please seelect from 1 - 3')
        access = int(input('Choose access: \n 1. Admin \n 2. User \n 3. Exit '))
    if access == 1:
        print('Welcome Admin!')
        Admin()
    elif access == 2:
        print('User Welcome!')
        Customer()
    elif access == 3:
        print('Good bye!!!')
        Exit()


if __name__ == '__main__':
    main()


