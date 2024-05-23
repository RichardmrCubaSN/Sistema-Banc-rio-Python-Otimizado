import textwrap

def menu():
    menu = """\n
    =============================================

            Sistema Bancario de Transações

    =============================================
           Seleccionar Opção de Preferencia

                  [d]\tDepositar
                  [s]\tSacar
                  [e]\tExtrato
                  [c]\tNova conta
                  [l]\tListar contas
                  [u]\tNovo usuário
                  [q]\tSair

    ==============================================
    => """

    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):
    print("======================================================")
    valor = float(input("Informe o valor do depósito: "))
    print("======================================================")

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"

        print("======================================================")
        print("\n=== Depósito realizado com sucesso! ===")
        print("======================================================")
    else:
        print("======================================================")
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        print("======================================================")

    return saldo, extrato



def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("======================================================")
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        print("======================================================")

    elif excedeu_limite:
        print("======================================================")
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        print("======================================================")

    elif excedeu_saques:
        print("======================================================")
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        print("======================================================")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("======================================================")
        print("\n=== Saque realizado com sucesso! ===")
        print("======================================================")

    else:
        print("======================================================")
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        print("======================================================")

    return saldo, extrato



def exibir_extrato(saldo, /, *, extrato):
    print("======================================================")
    print("\n                      EXTRATO                        ")
    print("======================================================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("======================================================")



def criar_usuario(usuarios):
    print("======================================================")
    cpf = input("Informe o seu CPF (somente número): ")
    print("======================================================")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("======================================================")
        print("\n@@@ Parece que já existe usuário com esse CPF! @@@")
        print("======================================================")
        return

    print("======================================================")
    print("                 Dados do Usuario                     ")
    print("======================================================")
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a data do seu nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("======================================================")

    print("======================================================")
    print("=== Usuário criado com sucesso! ===")
    print("======================================================")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_conta(agencia, numero_conta, usuarios):
    print("======================================================")
    cpf = input("Informe o CPF do usuário: ")
    print("======================================================")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("======================================================")
        print("\n=== Conta criada com sucesso! ===")
        print("======================================================")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("======================================================")
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    print("======================================================")



def listar_contas(contas):
    print("======================================================")
    print("                 Listado das Contas                   ")
    print("======================================================")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        print("======================================================")



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = 0
            depositar(saldo, valor, extrato)

        elif opcao == "s":
            print("======================================================")
            valor = float(input("Informe o valor do saque: "))
            print("======================================================")

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("======================================================")
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            print("======================================================")


main()