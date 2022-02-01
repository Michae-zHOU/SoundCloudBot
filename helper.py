import re

def get_number_from_str(s):
    return re.findall('[0-9]+', s)[0]