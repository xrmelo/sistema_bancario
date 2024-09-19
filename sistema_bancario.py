def menu():
    menu = """\n
===== MENU =====
1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair 
================
"""
    print(menu)


###---------------------------------------------------------------------

QTD_LIMITE_SAQUE_POR_DIA = 3
LIMITE_SAQUE         = 500
saldo = 0
extrato = ""
qtd_saques = 0

while True:
    menu()
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))
        # saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        # saldo, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
    elif opcao == 3:
        print("Extrato")
        ##exibir_extrato(saldo, extrato=extrato)
    elif opcao == 0:
        break
    else:
        print("Opção inválida")
# end while