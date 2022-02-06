numero=int(input("Insira um numero n "))
contador=1
acumulador=1
while(contador<=numero):    
    acumulador=contador*acumulador
    contador +=1
print(f"O fatorial de n será de {acumulador}")