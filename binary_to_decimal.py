import math

def binary_to_decimal(bit_string):
    bin_num = int(bit_string)
    dec_num = 0
    exp = 0
    while bin_num > 0:
        mod_val = bin_num % 10
        if mod_val == 1:
            dec_num += math.pow(2, exp)
        bin_num = bin_num // 10
        exp += 1
    return dec_num
            