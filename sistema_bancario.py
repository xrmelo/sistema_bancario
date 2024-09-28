# CONVENÇÕES 
# Mensagem de falha  usar :  @@@ mensagem...
# Mensagem de sucesso usar:  ### mensagem...

import os
from datetime import datetime


#------------------------------------------------------------------------------------------------------------------------
def menu():
    menu = """\n
+------ MENU -------+
! 1 - Depositar     !
! 2 - Sacar         !
! 3 - Extrato       !
! 4 - Criar Usuario !
! 0 - Sair          !
+-------------------+
"""
    print(menu)
    opcao = int(input("\nSELECIONE UMA OPÇÃO: "))
    return opcao
#------------------------------------------------------------------------------------------------------------------------

def depositar(saldo,extrato,/):
    print("\n>>> Depositar")  
    while True:
        valor = float(input("\nInforme o valor do depósito ou 0 para voltar: "))
        if valor == 0:
            break
        elif valor > 0:
            saldo += valor
            transacao = f" Depósito\t R$ {valor:.2f}\n"
            extrato = gerar_extrato(transacao,extrato)
            print(f"\n### Deposito de R$ {valor:.2f} realizado com sucesso.\nSeu saldo é R$ {saldo:.2f}")
        else:
            print("\nInforme um valor positivo ou 0 para voltar ")
    return saldo, extrato
#------------------------------------------------------------------------------------------------------------------------

def sacar(*,saldo,extrato,saque_qtd,LIMITE_SAQUE_QTD,LIMITE_SAQUE_VALOR):
   
    print("\n>> SACAR")
    while True:
        if saque_qtd == LIMITE_SAQUE_QTD:   
            input("@@@ Limite de saque alcançado, pressione <ENTER> para voltar")  
            break
       
        valor = float(input("\nInforme o valor para sacar ou 0 para voltar: "))    
          
        if valor == 0: break
        excedeu_saldo = valor > saldo
        excedeu_limite_saque_valor = valor > LIMITE_SAQUE_VALOR
        excedeu_limite_saque_qtd = saque_qtd >= LIMITE_SAQUE_QTD
        if excedeu_saldo:
            input(f"\n@@@ Saldo insuficiente !!! pressione <ENTER> para voltar")
            break
        elif excedeu_limite_saque_valor:
            print(f"\n@@@ Valor do saque excede o limite de R$ {LIMITE_SAQUE_VALOR:.0f}")
        elif excedeu_limite_saque_qtd:
            print("Número máximo de saques por dia é ",int(LIMITE_SAQUE_QTD))
            input("\nPressione <ENTER> para voltar")
            break
        elif valor > 0:
            saldo -= valor
            saque_qtd +=1
            transacao = f" Saque\t R$ {valor:.2f}\n"
            extrato = gerar_extrato(transacao,extrato)
            print("\n### Saque ",saque_qtd," de ", LIMITE_SAQUE_QTD, "realizado com sucesso !!!")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido.") 
    # end while
    return  saldo, extrato,saque_qtd
#------------------------------------------------------------------------------------------------------------------------

def gerar_extrato(transacao,extrato):
    data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    extrato += data+transacao
    return extrato

#------------------------------------------------------------------------------------------------------------------------
def imprimir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO =================")
    print("@@@ Não foram realizadas movimentações." if not extrato else extrato)
    print("==========================================")
    print(f"Saldo...: R$ {saldo:.2f}")
    print("==========================================")
    input("Pressione <ENTER> para voltar") 
#------------------------------------------------------------------------------------------------------------------------
def criar_usuario():
    print("\nPOR FAVOR INFORME: ")
    nome =            input("\nNome completo............................: ")
    data_nascimento = input("\nData de nascimento dd-mm-aaaa............: ")
    endereco =        input("\nEndereco - numero - bairro - cidade - UF.: ")
    return nome, data_nascimento,endereco
#------------------------------------------------------------------------------------------------------------------------
def cliente_ja_existe(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#------------------------------------------------------------------------------------------------------------------------
#                                                  MAIN
#------------------------------------------------------------------------------------------------------------------------
LIMITE_SAQUE_QTD = 3
LIMITE_SAQUE_VALOR = 500
saldo = 0
extrato = ""
saque_qtd = 0
usuarios = []
contas = []
while True: 
    os.system('cls')  
    print( "\nSaques/dia...: ",LIMITE_SAQUE_QTD)   
    print(f"\nMáximo/saque.: {LIMITE_SAQUE_VALOR:.2f}") 
    print(f"\nSeu Saldo é  :R$ {saldo:.2f}")
   
    opcao = menu()     
    if opcao == 1:
       saldo, extrato = depositar(saldo,extrato)
    elif opcao == 2:
        saldo, extrato,saque_qtd = sacar(
            saldo=saldo,
            extrato=extrato,
            saque_qtd=saque_qtd,
            LIMITE_SAQUE_QTD=LIMITE_SAQUE_QTD,
            LIMITE_SAQUE_VALOR=LIMITE_SAQUE_VALOR 
        )  
        #sacar(saldo,extrato,saque_qtd,LIMITE_SAQUE_QTD,LIMITE_SAQUE_VALOR)
    elif opcao == 3:
        #imprimir_extrato(saldo,extrato)
        imprimir_extrato(saldo,extrato=extrato)
    elif opcao == 4:
        cpf = input("\nInforme o CPF - somente numeros : ")
        if cliente_ja_existe(cpf,usuarios):
            input("\n@@@ Já existe cliente com este CPF pressione <ENTER> para voltar ")
        else:
            nome, data_nascimento, endereco = criar_usuario()
            usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
            input("\n### Cliente cadastrado com sucesso pressine <ENTER> para voltar")
    elif opcao == 0:
        break
    else:
        input("Opção inválida presione <Enter> para voltar")
#------------------------------------------------------------------------------------------------------------------------
