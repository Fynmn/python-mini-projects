print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++  ERROR-CORRECTION USING HAMMING CODE  ++++++")
print("+++++++++  this program converts a 3-digit  ++++++++")
print("++++++  hexadecimal code to its corresponding  +++++")
print("+++++++++         ASCII character          +++++++++")
print("+++++                                          +++++")
print("+++++++ Programmed by: Natalie Jane Pacificar ++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# The Algorithm for Hex to ASCII Character and Error Correction
# 1. Ask the user for a 3-digit hex code.
# 2. Convert the 3-digit hex code input to Binary(12-digit Hamming Code).
# Note: In some cases, when you convert a 3-digit hex code, it will only be equivalent to a 7, 8, 9, 10 or 11-digit Binary.
#       therefore we must add zeros on the beginning of the Binary code until it reaches 12 digits.
# 3. Map out the Data Bits in the 12-digit Hamming Code (8 Digits will be extracted).
# 4. Convert the extracted 8-digit Binary from our Data Bits to a Decimal Value.
# 5. **Error Correction** : Map out the Data Bits for every parity. Parity1, Parity2, Parity3, Parity4
# 6. Using Even Parity, add all the mapped out digits for every parity. After adding all the digits, if it results to an even number, then add 0. Else, add 1. **End of Error Correction**
# 7. Convert the Decimal value to its corresponding ASCII character.
# 8. Output the ASCII character.


#asks a 3-digit hex input from the user
x = True
while(x==True):
    hex_input = input("Enter a valid 3-digit hex code: ")

    if len(hex_input) != 3:
        hex_input = input("Enter a valid 3-digit hex code: ")
    else:
        break

scale = 16 #since hexadecimal is base 16
number_of_bits = 12 #will only work up to 8 bits of data AND 12-digit Hamming Code

#hex to binary (12-digit hamming code)
hamming_code = bin(int(hex_input, scale))[2:].zfill(number_of_bits)
print(f"Hex to Binary: {hamming_code}")

#map out the data bits from the hamming code
data_bits = [hamming_code[2], hamming_code[4], hamming_code[5], hamming_code[6], hamming_code[8], hamming_code[9], hamming_code[10], hamming_code[11]]
data_bits_res = ''.join(map(str, data_bits))
print(f"Data bits: {data_bits_res}")

print("\n---Error Correction---\n")

#Error Correction
parity_one = [hamming_code[0], hamming_code[2], hamming_code[4], hamming_code[6], hamming_code[8], hamming_code[10]]
parity_two = [hamming_code[1], hamming_code[2], hamming_code[5], hamming_code[6], hamming_code[9], hamming_code[10]]
parity_four = [hamming_code[3], hamming_code[4], hamming_code[5], hamming_code[6], hamming_code[11]]
parity_eight = [hamming_code[7], hamming_code[8], hamming_code[9], hamming_code[10], hamming_code[11]]

parities = [parity_one, parity_two, parity_four, parity_eight]

parity_count = []
parity_corrected = []

for x, i in enumerate(parities):
    for j in i:
        count = parities[x].count("1") # 3
    parity_count.append(count)

    #corrects the parity bit by adding the value 1 to the parity if it is odd and adding the value 0 if it is even
    if parity_count[x] % 2 == 0:
        parity_corrected.append("0")
    else:
        parity_corrected.append("1") 


for num,x in enumerate(parity_count):
    print(f"Parity {2**num}: {''.join(map(str, parities[num]))} - ({parity_count[num]}) - {parity_corrected[num]}")

#reverses the parity corrected values
parity_reverse = parity_corrected[::-1]
print(f"\nParity Reverse: {parity_reverse}")


#locates the Bit with Error
bit_with_error = int(''.join([str(value) for value in parity_reverse]), 2)
print(f"Bit with Error: {bit_with_error}")

#12 Digit Hamming Code
hamming_code = bin(int(hex_input, scale))[2:].zfill(number_of_bits)
print(f"Hex to Binary: {hamming_code}")

if bit_with_error == 0:
    #binary to decimal
    decimal_res = int(str(data_bits_res), 2)
    print(f"\nDecimal value extracted from the hex code: {decimal_res}")

    #decimal to ascii value
    ascii_value = chr(decimal_res)
    print(f"ASCII value: {ascii_value}\n")
elif bit_with_error <= 12:
    digit_to_flip = hamming_code[bit_with_error-1]
    print(f"Digit to Flip: {digit_to_flip}")
    
    if digit_to_flip == '0':
        flipped = '1'
    else:
        flipped = '0'
    
    new_hamming_code = list(hamming_code)
    new_hamming_code[int(bit_with_error-1)] = flipped
    
    corrected_hamming_code = ''.join(new_hamming_code)
    
    corrected_data_bits = [new_hamming_code[2], new_hamming_code[4], new_hamming_code[5], new_hamming_code[6], new_hamming_code[8], new_hamming_code[9], new_hamming_code[10], new_hamming_code[11]]
    corrected_data_bits_res = ''.join(map(str, corrected_data_bits))
    print(f"Data bits: {corrected_data_bits_res}")
    
    #binary to decimal
    corrected_decimal_res = int(str(corrected_data_bits_res), 2)
    print(f"\nDecimal value extracted from the hex code: {corrected_decimal_res}")

    #decimal to ascii value
    ascii_value = chr(corrected_decimal_res)
    print(f"ASCII value: {ascii_value}\n")

    
else:
    print("\nSorry. Cannot correct error because the error cannot be located.")





# Test
# N = 99e
# A = 891
# T = 0B4

#  0   0   0   0   0   0   0   0
# 128  64  32  16  8   4   2   1