import string
import re


def passcheck(password):
    if(len(password)<8):
        return True
    else:
        return False
def phone_number_validation(num):
    
    '''Check if the given variable contains a valid phone number or not'''
    
    check = re.compile("(0/91)?[7-9][0-9]{9}")
    
    if(check.match(num)):
        return True
    else:
        return False
    
def name_validation(check):
    
    ''' Checks if the given variable contains a valid name or not'''
    
    if len(check) == 0:
        return False
    
    discard = list(string.punctuation) + list(map(str,range(10)))
    
    for i in list(check):
         if i in discard:
            return False
        
    else:
        return True

def email_validation(check):
    
    '''Checks if the given variable contains a valid email or not'''
    
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    if(re.search(regex,check)):  
        return True  
    else:  
        return False
    
    
if __name__ == '__main__':
    
    n = input('Enter to check if it is a valid number or not(start with 91):')
    if phone_number_validation(n):
        print('The number is valid.')
    else:
        print('The number is invalid.')

    n = input('Enter to check if it is a valid name or not:')
    if name_validation(n):
        print('The name is valid.')
    else:
        print('The name is invalid.')
        
    n = input('Enter to check if it is a valid email or not:')
    if email_validation(n):
        print('The email is valid.')
    else:
        print('The email is invalid.')