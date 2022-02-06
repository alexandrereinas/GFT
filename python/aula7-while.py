contador=0
acumulador=0

limite = int(input("insira quantas notas você quer adicionar " ))

while contador<limite:


    nota=float(input("insira uma nota: "))
    acumulador += nota
    contador +=1
    media=(acumulador/limite)


print(f"A soma de todas as notas será: {acumulador:.2f}")
print(f"A média será: {media:.2f}")

