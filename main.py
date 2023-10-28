from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init()

print(Fore.MAGENTA + "Bem vindo a SUPER-CALCULADORA do Bruno!!")

def mostrar_menu():
    print(Fore.BLUE + "Selecione a operação:")
    print(Fore.BLUE + "1." + Fore.GREEN + " Soma")
    print(Fore.BLUE + "2." + Fore.YELLOW + " Subtração")
    print(Fore.BLUE + "3." + Fore.CYAN + " Multiplicação")
    print(Fore.BLUE + "4." + Fore.WHITE + " Divisão")
    print(Fore.BLUE + "5." + Fore.RED + " Sair" + Style.RESET_ALL)
def realizar_operacao(operacao, num1, num2):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 == 0:
            return "Erro: Divisão por zero"
        return num1 / num2

def formatar_numero(numero):
    # Verifica se o número tem casas decimais
    if int(numero) == numero:
        # Se não tiver casas decimais, exibe como um número inteiro
        return "{:,.0f}".format(numero)
    else:
        # Se tiver casas decimais, exibe com duas casas decimais
        return "{:,.2f}".format(numero)

def main():
    while True:
        mostrar_menu()

        try:
            operacao = int(input("Digite o número da operação desejada: "))

            if operacao == 5:
                print(Fore.RED + "Saindo...")
                break

            if operacao < 1 or operacao > 4:
                print(Fore.RED + "Opção inválida. Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            resultado = realizar_operacao(operacao, num1, num2)

            if isinstance(resultado, float):
                resultado_formatado = formatar_numero(resultado)
                print(Fore.GREEN + f"O resultado é: {resultado_formatado}")
            else:
                print(Fore.RED + resultado)

        except ValueError:
            print(Fore.RED + "Entrada inválida. Por favor, digite um número.")
        except ZeroDivisionError:
            print(Fore.RED + "Erro: Divisão por zero.")

if __name__ == "__main__":
    main()
