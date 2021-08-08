def reversev1(str): 
    reversed_string = str[::-1]
    return reversed_string

def reversev2(str):
    index = -1
    reversed_string = ''
    while index >= (len(str))*-1:
        reversed_string += str[index]
        index -= 1
    
    return reversed_string
def reversev3(str):
    if len(str) <= 1:
        return str
    return str[-1] + reversev3(str[:-1])

print(reversev3('awd'))
print(reversev2('perro'))
print(reversev1('straw'))