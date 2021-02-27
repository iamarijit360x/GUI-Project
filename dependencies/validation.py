def phone_number_validation(check):

''' Checks if the given variable contains a valid number or not '''
    
    try:
        n = 0
        for i in v:
            k = int(i)
            n += 1
            
        if n == 0:
            return True
        else:
            return False
    
    except:
        return False
    
if __main__ == '__name__':
    
    n = input('Enter to check if it is a valid number or not:')
    if phone_number_validation(n):
        print('The number is valid.')
    else:
        print('The number is invalid.')