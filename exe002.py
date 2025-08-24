import yfinance as yf
dat = yf.Ticker("PETR4.SA")
nome_empresa =  dat.info['longName'].strip().upper()
data = dat.history(period="5d")
preco_fechamento = data['Close'][0] 
print(nome_empresa)
print(f'Preço de fechamento: R$ {preco_fechamento:.2f}')