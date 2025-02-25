print("Esse software irá ajudar você a medir seu IMC")
peso = float(input("Informe o seu peso! "))
altura = float(input("Informe a sua altura! "))
imc = peso/(altura*altura)
if imc == 40:
    categoria = "Obesidade (grau III)"
elif imc >= 35:
    categoria = "Obesidade (grau II)"
elif imc >= 30:
    categoria = "Obesidade (grau I)"
elif imc >= 25:
    categoria = "Sobrepeso"
elif imc >= 18.50:
    categoria = "Peso Adequado"
elif imc >= 17:
    categoria = "Baixo peso (grau III)"
elif imc >= 16:
    categoria = "Baixo peso (grau II)"
elif imc < 15:
    categoria = "Baixo peso (grau I)"
print(f"Seu peso é", peso, "e sua altura é", altura, "portanto o seu indice de imc é %.2f" %imc)
print(f"A sua categoria é", categoria)