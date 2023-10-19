import sys

conv = {}
unconv = {}
for i in range(10):
    conv[chr(i+ord('0'))] = i
for i in range(10, 16):
    conv[chr(i+ord('A'))] = i

def hex_to_int(hexcode):
    converted = list()
    for i in hexcode:
        num = 0
        for j in i:
            num *= 16
            num += conv[j]
        converted.append(num)
    return converted

if(len(sys.argv) > 1):
    print(hex_to_int(sys.argv[1:]))
else:
    x = input("Enter: ")
    if(':' in x): y = hex_to_int(x.split(':'))
    elif(' ' in x): y = hex_to_int(x.split(' '))
    print(y)
    for i in y: print(i, end = '')

