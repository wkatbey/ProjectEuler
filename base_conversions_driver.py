import binary_to_decimal
import decimal_to_binary

print("1 - Binary to decimal")
print("2 - Decimal to binary")
menu = int(input("Select an option: "))

if menu == 1:
    bit_string = input('Enter a bit string: ')
    print(binary_to_decimal.binary_to_decimal(bit_string))
elif menu == 2:
    dec_num = int(input('Enter a decimal number: '))
    print(decimal_to_binary.decimal_to_binary(dec_num))


