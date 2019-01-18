import math

def decimal_to_binary(dec_num):
    bit_string = "";
    if dec_num == 0:
        return 0
    elif dec_num > 0:
        while dec_num > 0:
            remainder = dec_num % 2
            bit_string = str(remainder) + bit_string
            dec_num = dec_num // 2

        return bit_string
    

        
    
    

