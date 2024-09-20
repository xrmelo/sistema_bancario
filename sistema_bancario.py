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
    opcao = int(input("Selecione uma opção: "))
    return opcao
#------------------------------------------------------------------------------------------------------------------------
def depositar(saldo,extrato):
    print("\n### Depositar ###")
    
    while True:
        valor = float(input("\nInforme o valor do depósito ou 0 para cancelar: "))
        if valor == 0:
            break
        elif valor > 0:
            saldo += valor
            print(f"\nDeposito de R$ {valor:.2f} realizado com sucesso.\nSeu saldo é R$ {saldo:.2f}")
        else:
            print("\nInforme um valor positivo ou 0 para cancelar ")
        
    # end while
    # extrato += f"Deposito: R$ {valor:.2f}\n"
   
    return saldo, extrato
#------------------------------------------------------------------------------------------------------------------------
def sacar(saldo,extrato):
    print("em desenvolvimento")
    extrato += f"Saque...: R$ {valor:.2f}\n"
    return saldo,extrato
#------------------------------------------------------------------------------------------------------------------------
def extrato(saldo,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
#------------------------------------------------------------------------------------------------------------------------
#                                                  MAIN
#------------------------------------------------------------------------------------------------------------------------
QTD_LIMITE_SAQUE_POR_DIA = 3
LIMITE_SAQUE         = 500
saldo = 0
extrato = ""
qtd_saques = 0
while True:
    print(f"\nSeu saldo é R$ {saldo:.2f}")
    opcao = menu()   
    if opcao == 1:
       saldo, extrato = depositar(saldo,extrato)
    elif opcao == 2:
        print("Sacar em desenvolvimento")
        #valor = float(input("Informe o valor do saque: "))
        # saldo, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
    elif opcao == 3:
        print("Extrato em desenvolvimento")
        # extrato(saldo,extrato)
    elif opcao == 0:
        break
    else:
        print("Opção inválida")
#------------------------------------------------------------------------------------------------------------------------
