import string
import random

def random_captcha():
    
    s = 5
    sentence = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))
    return sentence

def registration_status_code(var_dict):
    
    #status_dict = {0:'Wrong Captcha', 1:'Username Invalid', 2:'Username Previously Registered', 3:'Password should be atleast 8 character long', 4:'Registration Done Successfully'}
    
    #return the status_code only
    
    pass

def login_status_code(var_dict):
    
    #status_dict = {0:'Wrong Captcha', 1:'Invalid Credentials'}
    
    #return the status_code only
    
    return {}  #just for testing