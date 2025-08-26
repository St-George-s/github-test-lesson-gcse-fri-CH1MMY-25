def linear_serch_first(items, target):
    found = False
    index_found = -1
    i = 0
    while i < len(items) and found == False:
        if items[1] == target:
            found = True
            index_found = i
        i = i+1
    return index_found


print(linear_serch_first([3, 7, 2 ,9, 5, 7], 7))
print(linear_serch_first([3, 7, 2 ,9, 5, 7], 4))