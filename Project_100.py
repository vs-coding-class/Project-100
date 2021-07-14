import sys

class bankATM(object):
    def __init__(self, name, operation):
        self.name = name
        self.operation = operation
    def authorize(self):
        for i in users:
            if(i == self.name):
                print('We have identified you. You are in the system.')
                break
            else:
                print('You are not in the system. Nice try, robber.')
    def transaction(self):
        if(self.operation == 'withdrawal'):
            print(f'We removed $1000 from your account.')
        elif(self.operation == 'insertion'):
            print(f'We added $1000 to your account.')
        else:
            print('Please put in something that the computer understands.')


users = ['Vinayak', 'Ira']

firstName = input('Please enter your first name... ')
operation = input("If you want to make a withdrawal, please type 'withdrawal'. If you want to put money in your account, please type 'insertion'. " )

person = bankATM(firstName, operation)
person.authorize()
person.transaction()