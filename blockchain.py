# initializing blockchain list
blockchain = []

# extract last value from blockchain
def get_last_block_value():
    """Returns the last value of the Blockchain"""
    return blockchain[-1]


# append latest value to blockchain
def add_value(transaction_amount, last_transaction=[1]):
    """Append a new value and the last value to the latest block
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction value. (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """Returns the input of the user (a new transaction amount) as a float. """
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


# output the blockchain list to the console
def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)


# test with values, prompt for input
tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_block_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invlaid, please pick a value from the list!')


print('Done!')


