import yfinance as yf
from colorama import init, Fore, Style,Back
init()


def mostrar_menu():
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT)
    print("\r" +"="*40)
    print("\rMENU PRINCIPAL")
    print("\t1. Sair do programa")
    print("\t2. Consultar Cotação da Bovespa")
    print("\t3. Tabuada!")
    print("\t4. Mostrar Menu")

    print("" +"="*40)
    print(Fore.WHITE + Back.BLACK + Style.NORMAL)

def obter_cotacao_bovespa(codigo_acao):
    dado = yf.Ticker(codigo_acao)
    nome_empresa = dado.info['longName'].strip().upper()
    historico = dado.history(period="5d")
    preco_fechamento = historico['Close'][0]
    saida = f"\n\r{nome_empresa}\n\rPreço de fechamento: R$ {preco_fechamento:.2f}\n\r"
    return saida

def tabuada():
    numero = int(input("Digite um número para ver a tabuada: "))
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT)
    print(f"Tabuada de {numero}  (multiplicação)".upper())
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT)
    cor = Fore.YELLOW + Back.BLACK
    for i in range(1, 11):
    
        if i % 2 == 0:
            cor = Fore.YELLOW + Back.BLACK
        else:
            cor = Fore.CYAN + Back.BLACK 

        print(f"{cor}{numero} × {i} = {numero * i}")
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT)

def exibir_tela_programa_principal():
    nome = input(Fore.YELLOW + Back.BLACK +"Digite seu nome: ")
    print(Fore.GREEN + Back.BLACK)
    print(f"Olá, {nome}! Bem vindo ao programa principal.")

    mostrar_menu()

    while True:        
                
        escolha = input("Escolha uma opção ")
        if escolha == '1':
            print(f"{nome}, você escolheu a opção 1. (Sair do programa)")
            break

        elif escolha == '2':
            print(f"{nome}, você escolheu a opção 2. (Consultar cotação da Bovespa)")
            codigo_acao = input("Digite o código da ação (Exemplo: PETR4.SA): ")
            try:
                resultado = obter_cotacao_bovespa(f'{codigo_acao}.SA')
                print(resultado)

            except:
                print("Erro ao obter a cotação. Verifique o código da ação e tente novamente.")

        elif escolha == '3':
            print(f"{nome}, você escolheu a opção 3. (Tabuada)")
            tabuada()
        
        elif escolha == '4':
            mostrar_menu()       

        
        else:
            print("Opção inválida. Tente novamente.")   


if __name__ == "__main__":
    exibir_tela_programa_principal()