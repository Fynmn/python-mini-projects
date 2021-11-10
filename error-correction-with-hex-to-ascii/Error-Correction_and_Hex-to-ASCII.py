print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++  ERROR-CORRECTION USING HAMMING CODE  ++++++")
print("+++++++++  this program converts a 3-digit  ++++++++")
print("++++++  hexadecimal code to its corresponding  +++++")
print("+++++++++         ASCII character          +++++++++")
print("+++++                                          +++++")
print("+++++++ Programmed by: Natalie Jane Pacificar ++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

#asks a 3-digit hex input from the user
x = True
while(x==True):
    hex_input = input("Enter a valid 3-digit hex code: ")

    if len(hex_input) != 3:
        hex_input = input("Enter a valid 3-digit hex code: ")
    else:
        break

scale = 16 #since hexadecimal is base 16
number_of_bits = 8 #will only work up to 8 bits of data

#hex to binary (12-digit hamming code)
hex_to_binary = bin(int(hex_input, scale))[2:].zfill(number_of_bits)
print(f"Hex to Binary: {hex_to_binary}")

#map out the data bits from the hamming code
data_bits = [hex_to_binary[2], hex_to_binary[4], hex_to_binary[5], hex_to_binary[6], hex_to_binary[8], hex_to_binary[9], hex_to_binary[10], hex_to_binary[11]]
data_bits_res = ''.join(map(str, data_bits))
print(f"Data bits: {data_bits_res}")

print("\n---Error Correction---\n")

#Error Correction
parity_one = [hex_to_binary[2], hex_to_binary[4], hex_to_binary[6], hex_to_binary[8], hex_to_binary[10]]
parity_two = [hex_to_binary[2], hex_to_binary[5], hex_to_binary[6], hex_to_binary[9], hex_to_binary[10]]
parity_four = [hex_to_binary[4], hex_to_binary[5], hex_to_binary[6], hex_to_binary[11]]
parity_eight = [hex_to_binary[8], hex_to_binary[9], hex_to_binary[10], hex_to_binary[11]]

parities = [parity_one, parity_two, parity_four, parity_eight]

parity_count = []
parity_corrected = []

for x, i in enumerate(parities):
    for j in i:
        count = parities[x].count("1")
    parity_count.append(count)

    #corrects the parity bit by adding the value 1 to the parity if it is odd and adding the value 0 if it is even
    if parity_count[x] % 2 == 0: 
        parity_corrected.append(0)
    else:
        parity_corrected.append(1) 


for num,x in enumerate(parity_count):
    print(f"Parity {2**num}: {''.join(map(str, parities[num]))} - ({parity_count[num]}) - {parity_corrected[num]}")


#binary to decimal
decimal_res = int(str(data_bits_res), 2)
print(f"\nDecimal value extracted from the hex code: {decimal_res}")

#decimal to ascii value
ascii_value = chr(decimal_res)
print(f"ASCII value: {ascii_value}\n")