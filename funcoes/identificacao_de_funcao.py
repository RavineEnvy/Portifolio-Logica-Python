def preencherInventario(lista):
    resposta = input("\nDeseja listar equipamentos? Digite \"S\" ou \"N\": ").upper()
    while True:
        if resposta == "S":
            equipamento = [input("\nEquipamento: "),
                           float(input("valor: ")),
                           int(input("Serial: ")),
                           input("Departamento: ")]
            lista.append(equipamento)
        elif resposta == "N":
            return

        resposta = input("\nDigite \"S\" para continuar ou \"N\" para cancelar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("\nNome........: ", elemento[0])
        print("Equipamento.: ", elemento[1])
        print("Serial......: ", elemento[2])
        print("Departamento: ", elemento[3])

def localizarListaPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    while True:
        for elemento in lista:
            if busca == elemento[0]:
                print("\nValor..: ", elemento[1])
                print("Serial.: ", elemento[2])
                return

            busca = input("\nDigite um equipamento válido: ")

def depreciacarPorNome(lista, porc):
    depreciar = input("\nDigite o nome do equipamento que deseja depreciar: ")
    while True:
        for elemento in lista:
            if depreciar == elemento[0]:
                print("\nValor antigo: ", elemento[1])
                elemento[1] = elemento [1] * (1-porc/100)
                print("Novo valor: ", elemento[1])
                return

        depreciar = input("\nDigite um equipamento válido: ")

def excluirPorSerial(lista):
    entrada = input("\nDigite o serial do equipamento que deseja excluir: ")
    while True:
        if not entrada.isdigit():
            entrada= input("Digite apenas números: ")
            continue

        serial = int(entrada)

        for elemento in lista:
            if serial == elemento[2]:
                print(f"\nO equipamento \"{elemento[0]}\" com o serial \"{elemento[2]}\" foi removido.")
                lista.remove(elemento)
                return "\nOs equipamentos restantes são: "

        entrada = input("Digite um serial válido: ")


def resumirValoresLista(lista):

    valores = []

    for elemento in lista:
        valores. append(elemento[1])
    if len(valores) > 0:
        print("\nMaior valor: ", max(valores))
        print("Menor valor: ", min(valores))
        print("Total de valores: ", sum(valores))