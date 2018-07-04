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


def get_user_input():
    """Returns the input of the user (a new transaction amount) as a float. """
    return float(input('Your transaction amount please: '))


# test with values, prompt for input
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(transaction_amount=tx_amount,
          last_transaction=get_last_block_value())

# output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)


print('Done!')


