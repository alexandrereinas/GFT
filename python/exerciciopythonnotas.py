contador=0
acumulador=0
while (contador<5):
    nota= float(input("Insira uma nota "))
    acumulador= nota+acumulador
    contador+=1
media=acumulador/5
print(f"media doa alunos foi de {media}")