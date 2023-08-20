saldo = 0
quant_saques = 0
extrato = []

menu = """SISTEMA BANCÁRIO 
1. SACAR 
2. DESPOSITAR 
3. VISUALIZAR EXTRATO
4. SAIR DO SISTEMA"""

def sacar(valor):
    global quant_saques 
    global saldo 

    if(quant_saques == 3):
        return "Já foi realizado o limite de 3 saques diários."
    elif(valor > 500):
        return "O valor máximo de saque é 500 reais."
    elif(saldo < valor):
        print(saldo,valor)
        return "Saldo insuficiente."
    else:
        quant_saques += 1
        saldo -= valor
        extrato.append(f"Tipo de operação: saque - Valor: R${valor:.2f}")
        return f"R${valor:.2f} foi sacado da conta. O saldo atual é R${saldo:.2f}"



def depositar(valor):
    global saldo 

    saldo += valor
    extrato.append(f"Tipo de operação: depósito - Valor: R${valor:.2f}")
    return f"R${valor:.2f} foi depositado na conta. O saldo atual é R${saldo:.2f}"

def visualizar_extrato():
    
    if(len(extrato) == 0):
        extrato.append("Não foram realizadas operações")
    
    extrato_str = ""
    for elem in extrato:
        extrato_str += elem + "\n"

    extrato_str += f"Saldo atual: R$ {saldo:.2f}"
    return extrato_str

while True:

    print(menu)
    print("Qual a sua escolha?")

   
    op = int(input())

    match op:
        case 1:
            print("Digite o valor a sacar:")
            valor = float(input())
            print(sacar(valor))
        case 2:
            print("Digite o valor a depositar:")
            valor = float(input())
            print(depositar(valor))
        case 3:
            print(visualizar_extrato())
        case 4:
            break




    

