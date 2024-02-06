1 - Requisitos:
O programa foi escrito em python e testado apenas usando a versão 3.11.3.
Além disso, foram consideradas apenas ações de empresas do Brasil ou EUA, pois considerei somente a cotação do Dólar em relação ao Real.

Para executar o programa, certifique-se de ter instaladas as bibliotecas yfinance e forex_python. Caso ainda não estejam instaladas, utilize os seguintes comandos no terminal:
    pip install yfinance
    pip install forex-python

A biblioteca yfinance é necessária para obtenção em tempo real das ações e a biblioteca forex_python é necessária para obtenção da cotação do Dólar.

2 - Como Usar:
    2.1 - Inserção Manual de Ações:
        As ações devem ser inseridas manualmente pelo usuário. O usuário deverá inserir o nome da ação, o preço de compra e a quantidade.
    2.2 - Obtenção do Preço Atual:
        O programa retornará o preço da ação em tempo real em R$, obtido através da API do Yahoo. Caso a ação seja internacional, o programa fará a conversão para a moeda brasileira.
    2.3 - Tratamento de exceções:
        Foi feito o tramento de exceções para ações não listadas.
        Além disso, o programa é case insensitive para as ações inseridas. Portanto, por exemplo, petr4 e PETR4 são equivalentes.

3 - Exemplo de uso:
No terminal:
>>python .\desafio.py
########## Calculadora de carteira de acoes ##########

Digite 1 para acao brasileira ou 0 para internacional: 1

Informe o ticker (codigo) da acao: petr4
Informe o preco (em R$) por acao no ato da operacao: 50
Informe a quantidade de acoes: 5

Digite "S" para adicionar mais acoes ou qualquer outra tecla para sair: s


Digite 1 para acao brasileira ou 0 para internacional: 1

Informe o ticker (codigo) da acao: irbr3
Informe o preco (em R$) por acao no ato da operacao: 25
Informe a quantidade de acoes: 4

Digite "S" para adicionar mais acoes ou qualquer outra tecla para sair: s


Digite 1 para acao brasileira ou 0 para internacional: 0

Informe o ticker (codigo) da acao: aapl
Informe o preco (em R$) por acao no ato da operacao: 1200
Informe a quantidade de acoes: 2

Digite "S" para adicionar mais acoes ou qualquer outra tecla para sair: s


Digite 1 para acao brasileira ou 0 para internacional: 0

Informe o ticker (codigo) da acao: ibm
Informe o preco (em R$) por acao no ato da operacao: 675
Informe a quantidade de acoes: 3

Digite "S" para adicionar mais acoes ou qualquer outra tecla para sair: s


Digite 1 para acao brasileira ou 0 para internacional: 1

Informe o ticker (codigo) da acao: teste
404 Client Error: Not Found for url: https://query2.finance.yahoo.com/v10/finance/quoteSummary/TESTE.SA?modules=financialData%2CquoteType%2CdefaultKeyStatistics%2CassetProfile%2CsummaryDetail&corsDomain=finance.yahoo.com&formatted=false&symbol=TESTE.SA&crumb=4W2yWwXI.lH
Erro: Nao foi possivel obter o preco atual para o ticker TESTE.SA. Verifique se o ticker esta correto.

Digite "S" para adicionar mais acoes ou qualquer outra tecla para sair: s


Digite 1 para acao brasileira ou 0 para internacional: 0

Informe o ticker (codigo) da acao: teste
404 Client Error: Not Found for url: https://query2.finance.yahoo.com/v10/finance/quoteSummary/TESTE?modules=financialData%2CquoteType%2CdefaultKeyStatistics%2CassetProfile%2CsummaryDetail&corsDomain=finance.yahoo.com&formatted=false&symbol=TESTE&crumb=4W2yWwXI.lH
Erro: Nao foi possivel obter o preco atual para o ticker TESTE. Verifique se o ticker esta correto.

Digite "S" para adicionar mais acoes ou qualquer outra tecla para sair: n


########## Resumo das acoes: ##########
        Acao: PETR4.SA
Preco de compra: R$50.00
Quantiade de acoes: 5
Total investido: R$250.00
Preco atual de cada acao: R$41.03
Retorno do investimento: R$205.15
Prejuizo de R$44.85


        Acao: IRBR3.SA
Preco de compra: R$25.00
Quantiade de acoes: 4
Total investido: R$100.00
Preco atual de cada acao: R$40.36
Retorno do investimento: R$161.44
Lucro de R$61.44


        Acao: AAPL
Preco de compra: R$1200.00
Quantiade de acoes: 2
Total investido: R$2400.00
Preco atual de cada acao: R$916.17
Retorno do investimento: R$1832.34
Prejuizo de R$567.66


        Acao: IBM
Preco de compra: R$675.00
Quantiade de acoes: 3
Total investido: R$2025.00
Preco atual de cada acao: R$915.87
Retorno do investimento: R$2747.62
Lucro de R$722.62




########## Resumo da carteira: ##########
Acoes investidas: PETR4.SA IRBR3.SA AAPL IBM
Quantidade de acoes: 14
Valor total investido: R$4775.00
Valor total em acoes: R$4946.55
Lucro de R$171.55
