# initializing blockchain list
blockchain = []

# extract last value from blockchain
def get_last_block_value():
    """Returns the last value of the Blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# append latest value to blockchain
def add_transaction(transaction_amount, last_transaction=[1]):
    """Append a new value and the last value to the latest block
    
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction value. (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]
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
    else: 
        print('-' * 20)

# a loop that can go through the chain to check validity
def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    return is_valid

waiting_for_input = True

while waiting_for_input:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_block_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invlaid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain')
        break
else: 
    print('User left!')


print('Done!')