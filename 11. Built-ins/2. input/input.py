# Enter your code here. Read input from STDIN. Print output to STDOUT
xk = input().split()
x, k = xk[0], xk[1]

# Evaluate the exppression
P = eval(input().replace("x", x))

# Check whether P is equal to k or not
print(True if P == int(k) else False)