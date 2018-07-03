blockchain = []

# extract last value from blockchain


def get_last_block_value():
    return blockchain[-1]


# append latest value to blockchain
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


# test with values
add_value(transaction_amount=2)
add_value(last_transaction=get_last_block_value(), transaction_amount=.6)
add_value(transaction_amount=20.2, last_transaction=get_last_block_value())

print(blockchain)
