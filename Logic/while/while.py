i = 0
while i < 5:
    i += 1
    print('puta vida')
else:
    print('Es verdad')



i = 0
while i <= 5:
    print(i)
    i+=1

invalid_number = True
while invalid_number:
   user_value = int(input('Please enter a number above 10: '))
   if user_value > 10:
       print(f'{user_value} es un buen numbero') 
       invalid_number = False
   else:
        print(f'{user_value} no es mayor a 10, intentelo de nuevo')

