blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(last_transaction=[0]):
    transaction_amount = get_user_input()
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input('Your transaction amount please: '))

add_value()
add_value(get_last_blockchain_value())
add_value(get_last_blockchain_value())
add_value(get_last_blockchain_value())

print(blockchain)
