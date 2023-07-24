#!/usr/bin/python3
"""Module contains validateUTF8 function"""

def validUTF8(data):
    """
    Checks if data is a valid UTF-8 character
    """
    count = 0
    for num in data:
        bin_num = format(num, '08b')
        if count == 0:
            for bit in bin_num:
                if bit == '0':
                    break
                count += 1
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (bin_num[0] == '1' and bin_num[1] == '0'):
                return False
        count -= 1
    if count == 0:
        return True
    return False
