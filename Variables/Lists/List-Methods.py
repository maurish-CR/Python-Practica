basket = [5,3,2,1,4]

#sorting
basket.sort() #acomada los elementos de la lista de menor a mayor (funciona con el alfabeto tambien)
print(sorted(basket)) #acomoda los elementos sin modificar la lista original

#overwrite
basket[1] = 2 #asignacion de nuevo valor para una posicion
basket[3:5] = [6, 7] #asignacion de nuevo valor para varias posiciones
#si se usa la opcion anterior se puede eliminar los elementos selecionados y agregar una nueva cantidad de elementos nuevos a la lista
print(basket)

#adding
basket.append(100) #inserta la final de la lista
basket.insert(1, 200) #inserta en el index que se le indique
basket.extend([12,22,95]) #inserta una lista de objetos al final de la lista deseada
print(basket)

#removing
basket.pop(2) #elimina en el index que se le indique,(default elimina el ultimo)
del basket[1] #elimina el elemento/s que se encuentre en el index indicado
basket.remove(7) #elimina el elemento con el valor que se le indique (Solo borra el primer elemento que se encuentre)
#basket.clear() #elimina todos los elementos de la lista
print(basket)

#in-not-in
print(100 in basket) #evalua si un elemento se encuentra dentro de la lista
print(100 not in basket) #evalua si un elemento NO se encuentra dentro de la lista


#reversing
basket.reverse() #invierte la lista (metodo)
print(basket)
baskte = basket[::-1] #invierte la lista de forma manual
print(basket)


#combination
basket2 = [88,8,26,61]
basket += basket2 #Union de 2 lista (Crea una nueva lista)*Version corta*
#basket = basket + basket2 #Union de 2 lista (Crea una nueva lista)*Version larga*
print(basket)

#count
print(basket.count(95)) #cuenta las veces que un elemento aparece en la lista
count = basket.count(22)
print(count)

#index
print(basket.index(88, 2, 10)) #busca la posicion del indice el valor que se le indica (ES EL INDEX DEL PRIMER VALOR)