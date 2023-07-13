menu = """
 ========MENU========
 1. EXTRATO
 2. SAQUE
 3. DEPÓSITO
 4. SAIR
 ===================="""
saldo = 0
limite = 500
extrato = ''
n_saques = 0
LIMITE_SAQUE = 3
deposito = 0

while True:
    opcao = int(input(menu + '\nSelecione uma opção: '))

    if opcao == 1:
        saques_restantes = LIMITE_SAQUE - n_saques
        print(
            f'''Valor em conta: R$ {saldo}.
            Saques realizados: {n_saques}
            Saques restantes: {saques_restantes}''')

    elif opcao == 2:
        valor_sacado = float(input('Insira o valor a sacar: '))
        
        if n_saques >= LIMITE_SAQUE and limite >= 500 or valor_sacado > 500:
            print('O limite diário de saques foi atingido!!! / O valor limite foi atingido!!! / Saque além do limite permitido!!!')
        else:
            saldo_restante = saldo - valor_sacado
            saldo = saldo_restante
            n_saques += 1
            print(f'''
            Valor sacado: R$ {valor_sacado}
            Saldo restante:R$ {saldo_restante} ''')
    elif opcao == 3:
        deposito = float(input("Insira o valor a ser depositado: "))
        saldo = deposito + saldo
        print(f""""
        Valor depositado: R$ {deposito}
        Saldo atual: R$ {saldo}""")
    else:
        print('Obrigado por usar nossos seviços!!!')
        break
