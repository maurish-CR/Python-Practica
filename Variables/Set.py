#en los Set no se repiten valores
my_set = {1,2,3,4,5}
my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1,2,3,4,5,5]
my_set = set(my_list)
print(my_set)


my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
#print(my_set.difference(your_set))
#my_set.discard(5)
#my_set.difference_update(your_set)
print(my_set)
print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))