def length_match(lst, number):
    count = 0
    for index in lst:   
        if len(index) == number:
            count += 1
    return count
    

def sum_from(num1, num2):
    total = 0
    for num in range(num1, num2+1):
        total += num
    return total


def same_index_values(lst1, lst2):
    same_value_lst = []
    index = 0
    while index <= len(lst1)-1:
        if lst1[index] == lst2[index]:
            same_value_lst.append(index)
        index += 1
    return same_value_lst



def same_index_values2(lst1, lst2):
    same_value_lst = []
    for i, v in enumerate(lst1):
        if v == lst2[i]:
            same_value_lst.append(i)
    return same_value_lst

print(same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]))
print(same_index_values2(["a", "b", "c", "d"], ["c", "b", "a", "d"]))