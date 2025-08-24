from colorama import init, Fore, Style,Back
init()

numero = 5
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