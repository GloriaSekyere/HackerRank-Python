# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    operands = input().split()
    a, b = operands[0], operands[1]

    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")