"""import locale

def formatar_salario_real(salario):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(salario, symbol=True, grouping=True)

print("Bem vindo ao software de calculo salárial da empresa SECURITY")
salario = float(input("Informe o seu salário!: "))
pontuacao = int(input("Informe a sua pontuação atingida!: "))
if pontuacao >= 1000:
    bonus = 500
    salario_total = salario + bonus
    salario_format = formatar_salario_real(salario)
    print("Com a sua pontuação o seu bônus será R$", bonus)
    print(f"Portanto, o valor do seu salário é: {salario_format}")
elif pontuacao >= 500:
    bonus = 300
    salario_total = salario + bonus
    salario_format = formatar_salario_real(salario)
    print("Com a sua pontuação o seu bônus será R$", bonus)
    print(f"Portanto, o valor do seu salário é: {salario_format}")
elif pontuacao >= 100:
    bonus = 150
    salario_total = salario + bonus
    salario_format = formatar_salario_real(salario)
    print("Com a sua pontuação o seu bônus será R$", bonus)
    print(f"Portanto, o valor do seu salário é: {salario_format}")
elif pontuacao >= 1:
    bonus = 20
    salario_total = salario + bonus
    salario_format = formatar_salario_real(salario)
    print("Com a sua pontuação o seu bônus será R$", bonus)
    print(f"Portanto, o valor do seu salário é: {salario_format}")
else:  
    bonus = 0
    salario_total = salario + bonus
    salario_format = formatar_salario_real(salario)
    print("Com a sua pontuação o seu bônus será R$", bonus)
    print(f"Portanto, o valor do seu salário é: {salario_format}")"""

import locale

def formatar_salario_real(salario):
    """Formata um valor numérico como uma string de moeda em reais."""
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(salario, symbol=True, grouping=True)

def obter_salario():
    """Obtém o salário do usuário e trata erros de entrada."""
    while True:
        try:
            salario_str = input("Informe o seu salário: ")
            salario_str = salario_str.replace(".", "").replace(",", "")
            salario = float(salario_str)
            if salario < 0:
                raise ValueError("Salário não pode ser negativo.")
            return salario
        except ValueError as e:
            print(f"Erro: {e}")

def obter_pontuacao():
    """Obtém a pontuação do usuário e trata erros de entrada."""
    while True:
        try:
            pontuacao = int(input("Informe a sua pontuação atingida: "))
            if pontuacao < 0:
                raise ValueError("Pontuação não pode ser negativa.")
            return pontuacao
        except ValueError as e:
            print(f"Erro: {e}")

def calcular_bonus(pontuacao):
    """Calcula o bônus com base na pontuação."""
    if pontuacao >= 1000:
        return 500
    elif pontuacao >= 500:
        return 300
    elif pontuacao >= 100:
        return 150
    elif pontuacao >= 1:
        return 20
    else:
        return 0

print("Bem vindo ao software de cálculo salarial da empresa SECURITY")

while True:
    salario = obter_salario()
    pontuacao = obter_pontuacao()
    bonus = calcular_bonus(pontuacao)
    salario_total = salario + bonus
    salario_format = formatar_salario_real(salario_total)

    print(f"Com a sua pontuação, o seu bônus será: {formatar_salario_real(bonus)}")
    print(f"Portanto, o valor do seu salário é: {salario_format}")

    reset = input("Deseja verificar outro salário? (sim/não)").lower()
    if reset != "sim":
        break

print("Obrigado por utilizar nosso programa!")