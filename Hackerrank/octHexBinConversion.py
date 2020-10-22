n = int(input())

width = len(bin(n).split('b')[1]) + 1

for i in range(1, n+1):
    decimal_val = str(i)
    octane_val = oct(i).split('o')[1]
    hex_val = hex(i).split('x')[1].upper()
    binvalue = bin(i).split('b')[1]
    print(decimal_val.rjust(width - 1) + octane_val.rjust(width) + hex_val.rjust(width) + binvalue.rjust(width))
