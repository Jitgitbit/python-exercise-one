# def power_fna():
#     print(2 ** 3)


def power_fnb(a, b):
    return a ** b

# power_fna()
print(power_fnb(2, 3))
##########################################################################################################################################################################
# Initializing our blockchain list 
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount]) 


def get_user_input():
    return float(input('Input your transaction amount please: '))       

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)