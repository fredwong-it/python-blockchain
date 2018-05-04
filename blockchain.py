blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(tx_amount, last_transaction=[0]):
    blockchain.append([last_transaction, tx_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_element():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_element()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please pick a value from the list!')


print('Done!')
