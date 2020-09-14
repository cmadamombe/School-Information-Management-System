""""
The function is used to calculate the employee numbers of the format: PA100200
"""
import random, re

def fill_with_zeros(e):
    """
    Used to fill integer values that are less than 100 with zeros EG: 2 becomes 002
    """
    ret = str(e)
    if len(str(e)) < 2:
        ret = f"00{str(e)}"
    elif len(str(e)) < 3:
        ret = f"0{str(e)}"
    else:
        ret = ret
    return ret

def increment_id(e):
    """Used to increment and format the id like so: EMxxx"""
    if e:
        h_int = re.search(r'^PA\s*0*(?P<gr>\d+)$', str(e), re.I).groupdict()["gr"]
        h_int2 = int(h_int)
        final_int = h_int2+1
        return f"PA {fill_with_zeros(final_int)}"
    else:
        return 'PA100200'
