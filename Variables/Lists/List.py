li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [True, 2 ,'a']


#building a list from another list
lst = [4,8,15,16,23,42]
def squares(number):
    lst_squ = []
    for v in number:
        lst_squ.append(v**2)
    return lst_squ

lst2 = squares(lst)
print(lst2)

def convert_to_floats(numbers):
    float_lst = []
    for num in numbers:
        float_lst.append(float(num))
    return float_lst
lst3 = convert_to_floats(lst)
print(lst3)

def even_or_odd(numbers):
    e_or_o = []
    for num in numbers:
        if num % 2 == 0:
            e_or_o.append(True)
        else:
            e_or_o.append(False)
    return e_or_o
lst4 = even_or_odd(lst)
print(lst4) 