def obter_cotacao(moeda):
    """Obtém a cotação da moeda do usuário."""
    while True:
        try:
            cotacao = float(input(f"Qual a cotação do {moeda}? "))
            return cotacao
        except ValueError:
            print("Cotação inválida. Digite um número.")

def converter_moeda(opcao, valor):
    """Converte o valor em reais para a moeda escolhida."""
    match opcao:
        case 1:  # Converter Real para Dólar
            cotacao = obter_cotacao("dólar")
            return valor / cotacao
        case 2:  # Converter Real para Euro
            cotacao = obter_cotacao("euro")
            return valor / cotacao
        case _:
            return None

def exibir_resultado(opcao, resultado):
    """Exibe o resultado da conversão."""
    if resultado is None:
        print("Opção inválida!")
    else:
        moeda = "Dólar" if opcao == 1 else "Euro"
        print(f"Valor convertido em {moeda}: {resultado:.2f}")

while True:
    try:
        valor = float(input("Digite o valor em Reais: "))
        print("Escolha a moeda para conversão:")
        print("Digite 1 para Dólar")
        print("Digite 2 para Euro")
        opcao = int(input("Entre com a opção desejada: "))

        resultado = converter_moeda(opcao, valor)
        exibir_resultado(opcao, resultado)

        reiniciar = input("Deseja converter mais algum valor? (sim/não) ").lower()
        if reiniciar != "sim":
            break
    except ValueError:
        print("Valor inválido. Digite um número.")

print("Obrigado por utilizar o conversor!")