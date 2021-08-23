# Using a for loop
list_of_lists = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            permutation = [i,j,k]
            #print(sum(permutation))
            if sum(permutation) != n:
                list_of_lists.append(permutation)
print(list_of_lists)

# Using list comprehensions
list_ = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k])!= n]
print(list_)