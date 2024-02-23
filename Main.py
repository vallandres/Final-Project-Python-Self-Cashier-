# Importing all methods from Transaction
from Transaction import *

transaction = Transaction() # Create an object of Transaction class

# Menu of Self Service Cashier
print('''
-----------------------------------------------
       WELCOME TO SELF CASHIER!!!
-----------------------------------------------
''')
while True:
    print('''
    Choose one of the following features:
    1: Add item.
    2: Check order/shopping cart.
    3: Delete item from shopping cart.
    4: Reset transaction (delete all items).
    5: Update item name.
    6: Update item quantity.
    7: Update item price.
    8: Calculate total price.
    9: Close program.
    ''')
    number = int(input('Input feature\'s number: '))
    if number == 1:
        transaction.add_item()
    elif number == 2:
        transaction.check_order()
        print('-----------------------------------------------')
    elif number == 3:
        transaction.delete_item()
        print('-----------------------------------------------')
    elif number == 4:
        transaction.reset_transaction()
        print('-----------------------------------------------')
    elif number == 5:
        transaction.update_item_name()
        print('-----------------------------------------------')
    elif number == 6:
        transaction.update_item_quantity()
        print('-----------------------------------------------')
    elif number == 7:
        transaction.update_item_price()
        print('-----------------------------------------------')
    elif number == 8:
        transaction.total_price()
        print('-----------------------------------------------')
    elif number == 9:
        print('''
        -----------------------------------------------
           Thank you for using self service cashier!
        -----------------------------------------------
        ''')
        break