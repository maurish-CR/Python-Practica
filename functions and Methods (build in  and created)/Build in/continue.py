def sum_positive(values):
    total = 0 
    for value in values:
        if value < 0:
            continue
        total += value
    return total
print(sum_positive([1,2,-3,4]))