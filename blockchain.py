# Initializing our blockchain list 
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

        Arguments:
            :transaction_amount: The amount that should be added.
            :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount]) 


def get_user_input():
    """ Returns the input of the user (a new transaction) as a float. """
    return float(input('Input your transaction amount please: '))       


# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

# Getting subsequent transactions and adding the value to the blockchain
while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output the blockchain list to the console
    for block in blockchain:
        print('Ouputting block')
        print(block)

print('Done!')