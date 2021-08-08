#Con funciones
Palabra = str(input('Ingrese una palabra: '))

def palindromo(A):
    Reversa = A[::-1]
    Validacion = ""
    if A.lower() == Reversa.lower():
        Validacion = f'{A} SI es un palindromo'
        return Validacion 
    else:
        Validacion = f'{A} NO es un palindromo'
        return Validacion 

print(palindromo(Palabra), end=" & ")

#--------------------------------*-----------------------------#

#Sin funciones
Palabra2 = str(input(('Palabra: ')))
Reversa = Palabra2[::-1]

if Palabra2.lower() == Reversa.lower():
    print(f'{Palabra2} si es un palindormo')
else:
    print(f'{Palabra2} no es un palindormo!')
    
