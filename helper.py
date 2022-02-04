import re

def get_number_from_str(s):
    emp_str = ""
    for m in s:
        if m.isdigit():
            emp_str = emp_str + m
    return int(emp_str)