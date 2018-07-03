blockchain = []

# extract last value from blockchain


def get_last_block_value():
    return blockchain[-1]


# append latest value to blockchain
def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction, transaction_amount])


# test with values
add_value(2, [1])
add_value(.6, get_last_block_value())
add_value(20.2, get_last_block_value())

print(blockchain)
