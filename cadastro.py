# Cria uma lista para armazenar os registros
registros = []

# Cores ANSI escape codes
COR_VERDE = '\033[92m'
COR_AMARELA = '\033[93m'
COR_AZUL = '\033[94m'
COR_MAGENTA = '\033[95m'
COR_VERMELHA = '\033[91m'
COR_RESET = '\033[0m'

# Função para imprimir texto colorido
def texto_colorido(texto, cor):
    return f"{cor}{texto}{COR_RESET}"

# Função para validar um CPF
def validar_cpf(cpf):
    if len(cpf) != 11:
        return False
    if not cpf.isdigit():
        return False
    # Adicione qualquer lógica de validação adicional aqui, se necessário
    return True

# Função para cadastrar um registro
def cadastrar_registro(tipo, cor):
    print(texto_colorido(f"Cadastro de {tipo}:", cor))
    registro = {"Tipo": tipo}
    
    if tipo == "Pessoa":
        registro["Nome"] = input("Nome: ")
        registro["Idade"] = int(input("Idade: "))
        cpf = input("CPF (11 dígitos numéricos): ")
        while not validar_cpf(cpf):
            print(texto_colorido("CPF inválido. Deve conter 11 dígitos numéricos.", COR_VERMELHA))
            cpf = input("CPF (11 dígitos numéricos): ")
        registro["CPF"] = cpf
        registro["E-mail"] = input("E-mail: ")
    elif tipo == "Produto":
        registro["Nome"] = input("Nome do Produto: ")
        registro["Preço"] = float(input("Preço: "))
        registro["Quantidade"] = int(input("Quantidade em Estoque: "))
    elif tipo == "Cliente":
        registro["Nome"] = input("Nome: ")
        registro["Endereço"] = input("Endereço: ")
        registro["Telefone"] = input("Telefone: ")
    
    registros.append(registro)
    print(texto_colorido(f"{tipo} cadastrado com sucesso!", cor))

# Função para listar os registros
def listar_registros():
    if not registros:
        print(texto_colorido("Nenhum registro encontrado.", COR_VERDE))
    else:
        print(texto_colorido("\nListagem de Registros:", COR_VERDE))
        for i, registro in enumerate(registros, start=1):
            print(f"Registro {i}:")
            for chave, valor in registro.items():
                print(f"{chave}: {valor}")
            print()

# Função principal
def main():
    while True:
        print(texto_colorido("\nEscolha o tipo de cadastro:", COR_VERDE))
        print(texto_colorido("1. Pessoa", COR_AMARELA))
        print(texto_colorido("2. Produto", COR_AZUL))
        print(texto_colorido("3. Cliente", COR_MAGENTA))
        print(texto_colorido("4. Visualizar Registros", COR_VERDE))
        print(texto_colorido("5. Sair", COR_VERMELHA))
        opcao = input(texto_colorido("Digite o número da opção desejada: ", COR_VERDE))

        if opcao == "1":
            cadastrar_registro("Pessoa", COR_AMARELA)
        elif opcao == "2":
            cadastrar_registro("Produto", COR_AZUL)
        elif opcao == "3":
            cadastrar_registro("Cliente", COR_MAGENTA)
        elif opcao == "4":
            listar_registros()
        elif opcao == "5":
            print(texto_colorido("Saindo...", COR_VERMELHA))
            break
        else:
            print(texto_colorido("Opção inválida. Tente novamente.", COR_VERMELHA))

if __name__ == "__main__":
    main()

# Mensagem divertida
print(texto_colorido("ESFREGADO NA SUA CARA", COR_VERDE))
