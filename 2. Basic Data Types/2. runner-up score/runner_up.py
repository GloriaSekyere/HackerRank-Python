if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    my_list = list(arr)
    my_list.sort()
    

    if n >= 2 and n <=10:
        
        for i in range(1, n+1):
            if (my_list[i-1] >= -100) and (my_list[i-1] <= 100):
                if my_list[i-1] < max(my_list):
                    maxi = my_list[i-1]
        print(maxi)
                
        
