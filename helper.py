import re

def get_number_from_str(s):
    return int(re.findall('[0-9]+', s)[0])