if __name__ == '__main__':
    s = input()
    if len(s) > 0 and len(s) < 1000:
        is_alnum = False
        is_alpha = False
        is_digit = False
        is_lower  = False
        is_upper = False
        
        for i in range(len(s)): 
            if s[i].isalnum():
                is_alnum = True
            if s[i].isalpha():
                is_alpha = True
            if s[i].isdigit():
                is_digit = True
            if s[i].islower():
                is_lower = True
            if s[i].isupper():
                is_upper = True
            
        print(is_alnum, is_alpha, is_digit, is_lower, is_upper, sep="\n")
            