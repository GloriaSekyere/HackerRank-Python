def print_formatted(n):
    if n >= 1 and n <= 99:
        padding = len(bin(n)[2:])
        for i in range(1,n+1):
            deci = str(i).rjust(padding)
            octal = oct(i)[2:].rjust(padding)
            hexa = hex(i)[2:].upper().rjust(padding)
            binary = bin(i)[2:].rjust(padding)
            print(deci, octal, hexa, binary, sep=" ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)