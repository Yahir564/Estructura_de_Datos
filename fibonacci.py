 #Primero definimos la funcion "fib"  
def fib (n):
    #Aqui si "n" es menor a 2 entonces la funcio se retorna a "n"
    if n < 2:
        return n 
    #Esta seria la funcion que define de fibonacci
    return fib (n-1) + fib (n-2)
#Aqui establecemos "s" como entero para poder ingresa el rango deseado
s = int(input("ingresa el rango tu lista:"))
#Despues el for lo utlizaremos para poder usar el rango de ello
for (x) in range (s):
    print (fib(x))
#Imprime el resultado deseado




