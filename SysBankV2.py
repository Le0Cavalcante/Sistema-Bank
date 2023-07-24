def menu():
    menu_text = """
    ========MENU========
    1. EXTRATO
    2. SAQUE
    3. DEPÓSITO
    4. NOVO USUÁRIO
    5. NOVA CONTA
    6. LISTAR CONTAS
    7. SAIR
    ====================
    """
    return int(input(menu_text + "\nSelecione uma opção: "))

def depositar(saldo, deposito):
    if deposito > 0:
        saldo += deposito
        print(f'Depósito realizado com sucesso!!! \nSaldo atualizado: R$ {saldo:.2f}')
    else:
        print('Valor inválido!!!')
    return saldo

def sacar(*, saldo, saque, limite, n_saques, l_saque):
    if saque > saldo:
        print('Saldo Insuficiente!!')
    elif saque > limite:
        print('O valor do saque excedeu o limite!!!')
    elif saque > 0:
        saldo -= saque
        n_saques += 1
        print(f'''Saque realizado com sucesso!!
        Saques realizados: {n_saques}
        Saques restantes: {(l_saque - n_saques)}''')
    return saldo, n_saques

def exibir_extrato(saldo, extrato):
    print(f'Valor em conta: R$ {saldo:.2f}')

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def criar_usuario(usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Usuário já existente.')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento: ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla Estado): ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso!')

def criar_conta(agencia, n_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Conta criada com sucesso!!!')
        return {'Agência':agencia, 'n_conta':n_conta, 'usuario':usuario}
    print('Usuário não cadastrado!!')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência: \t{conta['agencia']}
            C/C: \t {conta['n_conta']}
            Titular: \t{conta['usuario']['nome']}
        '''
        print(linha)

def main():
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    n_saques = 0
    LIMITE_SAQUE = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            print('Exibir Extrato selecionado:')
            exibir_extrato(saldo, extrato=None)  # Extrato is not used, so we can pass None.
        elif opcao == 2:
            print('Saque selecionado:')
            saque = float(input('Digite o Valor a ser sacado: '))
            saldo, n_saques = sacar(
                saldo=saldo,
                saque=saque,
                limite=limite,
                n_saques=n_saques,
                l_saque=LIMITE_SAQUE,
            )
        elif opcao == 3:
            print("Depósito selecionado!!")
            deposito = float(input("Informe o valor a ser depositado: "))
            saldo = depositar(saldo, deposito)

        elif opcao == 4:
            print('Criar novo usuário selecionado!!')
            criar_usuario(usuarios)

        elif opcao == 5:
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)
        else:
            print("Obrigado por utilizar nossos serviços!!!")
            break


main()
