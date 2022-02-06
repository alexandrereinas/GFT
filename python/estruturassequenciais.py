salario_mensal=float(input("Insira o seu salario mensal R$  "))
despesa_mensal=float(input("Insira a sua despesa mensal R$  "))
salario_total= salario_mensal*12
despesa_total=despesa_mensal*12
quantidade_economizada =salario_total-despesa_total
print(f"A quantidade economizada em um ano foi de R$ {quantidade_economizada:.2f}")