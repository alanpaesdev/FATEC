import requests
import locale

# Configura o locale para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def obter_cotacao(moeda):
    """Obtém a cotação da moeda em tempo real."""
    url = "https://api.hgbrasil.com/finance/quotations?key=7fe94795"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if moeda == 1:
            cotacao = dados['results']['currencies']['USD']['buy']
            return cotacao
        elif moeda == 2:
            cotacao = dados['results']['currencies']['EUR']['buy']
            return cotacao
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter cotação: {e}")
        return None

def converter_moeda(valor, opcao):
    """Converte o valor em reais para a moeda escolhida e retorna a cotação."""
    cotacao = obter_cotacao(opcao)
    if cotacao:
        if opcao == 1:  # Converter Real para Dólar
            valor_convertido = valor / cotacao
            valor_em_reais = valor
            return valor_convertido, cotacao, valor_em_reais
        elif opcao == 2:  # Converter Real para Euro
            valor_convertido = valor / cotacao
            valor_em_reais = valor
            return valor_convertido, cotacao, valor_em_reais
    return None, None, None

while True:  # Loop principal para reiniciar o programa
    valor_str = input("Digite o valor em Reais: ")
    valor_str = valor_str.replace(".", "").replace(",", "")  # Remove pontos e vírgulas
    try:
        valor = float(valor_str)
    except ValueError:
        print("Valor inválido. Digite um número.")
        continue  # Volta ao início do loop

    print("Escolha a moeda para conversão:")
    print("Digite 1 para Dólar")
    print("Digite 2 para Euro")
    opcao = int(input("Entre com a opção desejada: "))

    resultado, cotacao_do_dia, valor_em_reais = converter_moeda(valor, opcao)

    if resultado is None:
        print("Opção inválida ou erro na cotação.")
    else:
        if opcao == 1:
            print(f"Cotação do Dólar: {cotacao_do_dia:.2f}")
            print(locale.format_string("Valor em Dólar: U$%.2f", resultado, grouping=True))
            print(locale.format_string("Valor em Reais: R$%.2f", valor_em_reais, grouping=True))
        elif opcao == 2:
            print(f"Cotação do Euro: {cotacao_do_dia:.2f}")
            print(locale.format_string("Valor em Euro: €%.2f", resultado, grouping=True))
            print(locale.format_string("Valor em Reais: R$%.2f", valor_em_reais, grouping=True))

    reiniciar = input("Deseja realizar outra conversão? (sim/não): ").lower()
    if reiniciar != "sim":
        print("Programa encerrado, obrigado por utilizar o cotador!s.")
        break  # Sai do loop principal e finaliza o programa