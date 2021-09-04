def average(array):
    unique_list = list(set(array))
    total, length = sum(unique_list), len(unique_list)
    average = total / length
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)