import yfinance as yf

def obter_cotacao_bovespa(codigo_acao):
    dado = yf.Ticker(codigo_acao)
    nome_empresa = dado.info['longName'].strip().upper()
    historico = dado.history(period="5d")
    preco_fechamento = historico['Close'][0]
    saida = f"\n\r{nome_empresa}\n\rPreço de fechamento: R$ {preco_fechamento:.2f}\n\r"
    return saida