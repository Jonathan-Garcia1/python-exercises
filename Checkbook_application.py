import json
import os

#create welcome message variable
welcome = '''~~~ Welcome to your terminal checkbook! ~~~'''

options = '''What would you like to do?

1) view current balance
2) record a debit (withdraw)
3) record a credit (deposit)
4) exit'''

#create task list
task_list = [1,2,3,4]

#define functions to view balance
def debits():
    b = balance
    debit = int(input('How much is the debit? '))
    b -= debit
    return b

def credits():
    b = balance
    debit = int(input('How much is the debit? '))
    b += debit
    return b

#make withdrawals, and make deposits

cb_file = 'checkbook.json'

#check if file exists using os library
if os.path.exists(cb_file):

    with open (cb_file, 'r') as f:
    
        balance = json.load(f)

#otherwise, set balance to 0
else:
    balance = 0

print(type(balance))


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


