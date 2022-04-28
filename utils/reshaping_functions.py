import re
from numpy import NaN
import pandas as pd
from datetime import datetime


def find_resume(description_lst):
    
    start = False
    text = ''
    
    regex = re.compile(r'\w+:$')
    
    try:
        for i in range(len(description_lst)):
            
            if (description_lst[i] == 'Resumé:') | (description_lst[i] == 'Forespørgslen:'):
                    return description_lst[i+1]
            elif description_lst[i] == 'Forslag til vedtagelse:':
                 start = True
            elif (re.search(regex, description_lst[i]) != None) & (start == True):
                return text
            elif start == True:
                text += description_lst[i]
                
    except:
        return NaN
    return NaN


def find_date(description_lst):
    try:
        regex = re.compile(r"\d\d-\d\d-\d{4}")
        found = ""
        for element in description_lst:
            if re.search(regex, element) != None:
                found = re.search(regex, element)
                
        found = datetime.strptime(found[0], "%d-%m-%Y").date()
        return found
    except:
        return NaN
    
    