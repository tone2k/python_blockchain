blockchain = [[1]]

# extract last value from blockchain
def get_last_block_value():
    return blockchain[-1]

# append latest value to blockchain
def add_value(transaction_amount): 
    blockchain.append([get_last_block_value(), transaction_amount])
    print(blockchain)


# test with values
add_value(2)
add_value(.6)
add_value(20.2)