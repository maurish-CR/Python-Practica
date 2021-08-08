lst = [1,2,3,4]
print(lst[::-1])

i = -1
while i >= len(lst)*-1:
    print(lst[i])
    i-=1


reverse = reversed(lst)
print(reverse)

lst.reverse() 
print(lst)