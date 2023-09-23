import json
import os

#create welcome message variable
welcome = '''~~~ Welcome to your terminal checkbook! ~~~'''

options = '''What would you like to do?

1) view current balance
2) record a debit (withdraw)
3) record a credit (deposit)
4) view transactions (history)
5) exit'''

#create task list
task_list = [1,2,3,4,5]
trans = []

#define functions to view balance
def debits():
    # create a new variable b, set it to the original balance
    b = balance
    # use the input to set debit variable
    debit = int(input('How much is the debit? '))
    # b(balance) will subtract debit from
    b -= debit
    #set new dictionary transactions to the dictionary with the debited amount
    new_dic_trans = {"type": "debit", "amount": debit}
    # open the transactions file as tf
    with open (trans_file, 'w') as tf:
        #set the file contents to dic_trans
        #dic_trans = json.load(tf)
        #update the original transactions dictionaries with the new transaction (append)
        dic_trans.append(new_dic_trans)
        json.dump(dic_trans, tf, indent=4)

    return b

def credits():
    b = balance
    debit = int(input('How much is the debit? '))
    b += debit
    return b

#make withdrawals, and make deposits

cb_file = 'checkbook.json'
trans_file = 'transactions.json'

#check if file exists using os library
if os.path.exists(cb_file):

    with open (cb_file, 'r') as f:
    
        balance = json.load(f)

#otherwise, set balance to 0
else:
    balance = 0

#load the transactions dictionary from the transactions file
if os.path.exists(trans_file):
    with open (trans_file, 'r') as tf:
        dic_trans = json.load(tf)
else:
    dic_trans = {}

#print welcome message
print(welcome)

#create the logic
while True:
    #ask for input 
    print(options)
    curr_task = int(input('Your choice? '))
    #check if the option selected is part of the avialable tasks
    if curr_task in task_list:
        #check if the task is 1
        if curr_task == 1:
            #print the current balance
            print(balance)
            print()
        elif curr_task == 2:
            balance = debits()
            print(balance)
        elif curr_task == 3:
            balance = credits()
            print(balance)
        elif curr_task == 4:
            print('Transactions history')
            for transaction in dic_trans:
                print(transaction["type"], "\t", transaction["amount"])
        elif curr_task == 5:
            print()
            if input('save changes? Y/N ') == 'Y':
                with open (cb_file, 'w') as f:
                    json.dump(balance, f)
                print('changes saved, have a great day!')
            else:
                print('Thanks, have a great day!')
            break

    #if not part of the options, say invalid choice and ask again
    else:
        print('Invalid choice: ')
        continue
    
#with open (cb_file, 'w') as f:
#    json.dump(balance, f)