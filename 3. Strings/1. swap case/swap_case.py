def swap_case(s):
    if len(s) > 0 and len(s) <= 1000:
        new_s = s.swapcase()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
