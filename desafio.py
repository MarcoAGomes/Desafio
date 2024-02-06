# Autor: Marco Antonio Machado Gomes
# Data: 04/02/2024
# Projeto: Calculadora de Carteira de Ações

import yfinance as yf
from forex_python.converter import CurrencyRates

#função que retorna o preço atual de determinada ação a partir da API do Yahoo
def busca_acao(ticker):
    try:
        codigo = yf.Ticker(ticker)
        preco_atual = codigo.info['currentPrice']
        return preco_atual
    except KeyError:
        print(f"Erro: Nao foi possivel obter o preco atual para o ticker {ticker}. Verifique se o ticker esta correto.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

#função para converter o preço de uma ação em dólar para real a partir da API The Forex rates API
def converter_dolares_para_brl(valor):
    cr = CurrencyRates()
    output = cr.convert("USD", "BRL", valor)
    return output


lista_ticker = []
lista_preco_acao = []
lista_quantiade_acao = []
lista_preco_acao_atual = []


print("########## Calculadora de carteira de acoes ########## \n")

add_acoes = True

while(add_acoes):

    acao_BR = int(input("Digite 1 para acao brasileira ou 0 para internacional: "))

    ticker = input("\nInforme o ticker (codigo) da acao: ")
    ticker = ticker.upper()
    
    if (acao_BR):
        ticker += ".SA"

    preco_atual_ticker = busca_acao(ticker)
    if (preco_atual_ticker):
        preco_por_acao = float(input("Informe o preco (em R$) por acao no ato da operacao: "))
        quantidade_acao = int(input("Informe a quantidade de acoes: "))

        if (not acao_BR):
            preco_atual_ticker = converter_dolares_para_brl(preco_atual_ticker)

        lista_ticker.append(ticker)
        lista_preco_acao.append(preco_por_acao)
        lista_quantiade_acao.append(quantidade_acao)
        lista_preco_acao_atual.append(preco_atual_ticker)
    
    else:
        None

    continuar = input("\nDigite \"S\" para adicionar mais acoes ou qualquer outra tecla para sair: ")
    print("\n")
    continuar = continuar.upper()
    if (continuar!="S"):
        add_acoes = False
        break
    else:
        continue


investimento_total_carteira = 0
retorno_total_carteira = 0

#Ações individuais
print("########## Resumo das acoes: ########## ")
for acao in range(len(lista_ticker)):
    print(f"\tAcao: {lista_ticker[acao]}")
    print(f"Preco de compra: R${lista_preco_acao[acao]:.2f}")
    print(f"Quantiade de acoes: {lista_quantiade_acao[acao]}")
    
    total_investido = lista_quantiade_acao[acao]*lista_preco_acao[acao]
    total_retorno = lista_quantiade_acao[acao]*lista_preco_acao_atual[acao]

    print(f"Total investido: R${total_investido:.2f}")
    print(f"Preco atual de cada acao: R${lista_preco_acao_atual[acao]:.2f}")
    print(f"Retorno do investimento: R${total_retorno:.2f}")
    
    qtde_lucro = total_retorno-total_investido

    lucro = "Lucro" if qtde_lucro > 0 else "Prejuizo"
    
    print(f"{lucro} de R${abs(qtde_lucro):.2f}")

    investimento_total_carteira += total_investido
    retorno_total_carteira += total_retorno

    print("\n")

#Carteira completa
print("\n")
print("########## Resumo da carteira: ########## ")
print("Acoes investidas: ",end="")
for i in lista_ticker:
    print(i,end=" ")
print(f"\nQuantidade de acoes: {sum(lista_quantiade_acao)}")
print(f"Valor total investido: R${investimento_total_carteira:.2f}")
print(f"Valor total em acoes: R${retorno_total_carteira:.2f}")

qtde_lucro_total = retorno_total_carteira-investimento_total_carteira
lucro_total = "Lucro" if qtde_lucro_total > 0 else "Prejuizo"

print(f"{lucro} de R${abs(qtde_lucro_total):.2f}")

