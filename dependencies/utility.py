import string
import random

def random_captcha():
    
    s = 8
    sentence = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))
    return sentence