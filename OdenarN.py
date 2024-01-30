lista = [2,1,3,4,5,3,9,1,1,500,-2]
 
for posicion in range(len(lista)):
    minimum = posicion
    for num in range(posicion, len(lista)):
       if lista[num] < lista[minimum]:
           minimum = num
    lista[posicion], lista[minimum] = lista[minimum], lista[posicion]
 
print(lista)

    


    
    