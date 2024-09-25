import os

def menu():
    menu = """\n
=====<<< MENU >>>=====
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
    print("\n>>> Depositar")
    
    while True:
        valor = float(input("\nInforme o valor do depósito ou 0 para voltar: "))
        if valor == 0:
            break
        elif valor > 0:
            saldo += valor
            print(f"\nDeposito de R$ {valor:.2f} realizado com sucesso.\nSeu saldo é R$ {saldo:.2f}")
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nInforme um valor positivo ou 0 para voltar ")
        
    # end while
    # extrato += f"Deposito: R$ {valor:.2f}\n"
   
    return saldo, extrato
#------------------------------------------------------------------------------------------------------------------------
def sacar(saldo,extrato,saque_qtd,LIMITE_SAQUE_QTD,LIMITE_SAQUE_VALOR):
   
    print("\n>> SACAR")
    while True:
        if saque_qtd == LIMITE_SAQUE_QTD:   
            input("Limite de saque alcançado, pressione <ENTER> para voltar")  
            break
       
        valor = float(input("\nInforme o valor para sacar ou 0 para voltar: "))    
          
        if valor == 0: break
        excedeu_saldo = valor > saldo
        excedeu_limite_saque_valor = valor > LIMITE_SAQUE_VALOR
        excedeu_limite_saque_qtd = saque_qtd >= LIMITE_SAQUE_QTD
        if excedeu_saldo:
            print(f"\nSaldo insuficiente !!!")
            break
        elif excedeu_limite_saque_valor:
            print(f"Valor do saque excede o limite de R$ {LIMITE_SAQUE_VALOR:.0f}")
        elif excedeu_limite_saque_qtd:
            print("Número máximo de saques por dia é ",int(LIMITE_SAQUE_QTD))
            input("\nPressione <ENTER> para voltar")
            break
        elif valor > 0:
            saldo -= valor
            saque_qtd +=1
            print("\nSaque ",saque_qtd," de ", LIMITE_SAQUE_QTD, "realizado com sucesso !!!")
            extrato += f"Saque...: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.") 
    # end while
    return  saldo, extrato,saque_qtd
#------------------------------------------------------------------------------------------------------------------------
def imprimir_extrato(saldo,extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("==========================================")
    print(f"Saldo...: R$ {saldo:.2f}")
    print("==========================================")
#------------------------------------------------------------------------------------------------------------------------
#                                                  MAIN
#------------------------------------------------------------------------------------------------------------------------
LIMITE_SAQUE_QTD = 3
LIMITE_SAQUE_VALOR = 500
saldo = 0
extrato = ""
saque_qtd = 0
saque_limite = 0
while True: 
    os.system('cls')  
    print( "\nSaques/dia...: ",LIMITE_SAQUE_QTD)   
    print(f"\nMáximo/saque.: {LIMITE_SAQUE_VALOR:.2f}") 
    print(f"\nSeu Saldo é  :R$ {saldo:.2f}")
   
    opcao = menu()     
    if opcao == 1:
       saldo, extrato = depositar(saldo,extrato)
    elif opcao == 2:
        saldo, extrato,saque_qtd = sacar(saldo,extrato,saque_qtd,LIMITE_SAQUE_QTD,LIMITE_SAQUE_VALOR)
    elif opcao == 3:
        imprimir_extrato(saldo,extrato)
        input("Pressione <ENTER> para voltar") 
    elif opcao == 0:
        break
    else:
        print("Opção inválida")
#------------------------------------------------------------------------------------------------------------------------
