#10/02/25 primeira aula de programação
#Comentario professor, Python declara variaveis automaticamente

def obter_notas(qtd_notas):
    """Obtém as notas do usuário."""
    notas = []
    for i in range(qtd_notas):
        while True:
            try:
                nota = float(input(f"Entre com a nota {i + 1}: "))
                if not 0 <= nota <= 10:
                    raise ValueError("Nota inválida. Deve estar entre 0 e 10.")
                notas.append(nota)
                break
            except ValueError:
                print("Nota inválida. Digite um número entre 0 e 10.")
    return notas


def calcular_media(notas):
    """Calcula a média das notas."""
    return sum(notas) / len(notas)


def obter_frequencia():
    """Obtém a frequência do usuário."""
    while True:
        try:
            frequencia = int(input("Entre com a frequência: "))
            if not 0 <= frequencia <= 100:
                raise ValueError("Frequência inválida. Deve estar entre 0 e 100.")
            return frequencia
        except ValueError:
            print("Frequência inválida. Digite um número entre 0 e 100.")


def determinar_status(media, frequencia):
    """Determina o status do aluno."""
    if media >= 6 and frequencia >= 75:
        return "Aprovado"
    elif media >= 4 and frequencia >= 75:
        return "Exame Geral"
    else:
        return "Reprovado"


while True:
    try:
        print("Esse programa irá auxiliar você a calcular a média")
        qtd_notas = int(input("Informe a quantidade de notas que deseja obter a média: "))
        notas = obter_notas(qtd_notas)
        frequencia = obter_frequencia()

        media = calcular_media(notas)
        status = determinar_status(media, frequencia)

        print(f"Sua média foi: {media:.2f}")
        print(f"Sua frequência: {frequencia}")
        print(status)

        reiniciar = input("Deseja continuar a obter média de notas? (sim/não)").lower()
        if reiniciar != "sim":
            break
    except Exception as e:
        print(f"Erro: {e}")

print("Obrigado por utilizar o programa!")