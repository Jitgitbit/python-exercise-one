# Initializing our blockchain list 
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'ThierryD'
# participants = set(['ThierryD'])
# The line above means the same as underhere, Python understands that this is a set !
participants = {'ThierryD'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

        Arguments:
            :sender: The sender of the coins.
            :recipient: The recipient of the coins.
            :amount: The amount of coins sent with the transaction (default = 1.0).
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    # print(' -> Printing hashed_block: ', hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction) as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter your transaction amount please: ')) 
    return tx_recipient, tx_amount    


def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input('Enter your choice: ')
    return user_input


def print_blockchain_elements():
    """ Output all blocks of the blockchain. """
    for block in blockchain:
        print(' -> Ouputting block:', block)
    else:
        print('-' * 50)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise!"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Note that the optional sender argument is skipped and therefore we have a named amount argument call !
        add_transaction(recipient, amount=amount)
        print(' -> Printing open_transactions: ', open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'ThierryD', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('---> Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('---> Invalid blockchain!')
        break
    print('---> Choice registered!')
else:
    print('---> User left!')


print('===> Done!')