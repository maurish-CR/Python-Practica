#Iteracion con for
dinner = 'Steak and Potatoes'

for i in dinner:
    print(i)


print()
#Iteracion con condicion logica
values = [3,6,9,12,15,18,21,24]
other_values = [5,10,15,20,25,30]

def odd_sum(numbers):
    total = 0
    for i in numbers:
        if i % 2 != 0:
            total += i
    return total
print(odd_sum(other_values))

def greatest_number(numbers):
    greatest = 0
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest

print(greatest_number([4,5,5]))