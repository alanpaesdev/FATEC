import random

def jogar_par_impar():
    numero = int(input("Informe um número entre 1 e 5: "))
    print("O seu número escolhido foi", numero)
    escolha = input("Você quer Par ou Ímpar? ").lower()
    print("Agora é a minha vez de escolher um número!")

    numero_aleatorio = random.randint(1, 5)
    print("Meu número é", numero_aleatorio)
    par_impar = numero + numero_aleatorio

    def verificar_par_impar(soma):
        if soma % 2 == 0:
            return "Par"
        else:
            return "Ímpar"

    resultado = verificar_par_impar(par_impar)
    print("A soma dos números é:", par_impar, "que é", resultado)

    if escolha == resultado.lower():
        print("Você ganhou!")
    else:
        print("Eu ganhei!")

while True:
    jogar_par_impar()
    reiniciar = input("Deseja jogar novamente? (sim/não): ").lower()
    if reiniciar != "sim":
        break

print("Obrigado por jogar!")