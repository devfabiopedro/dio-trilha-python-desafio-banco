import os

# Armazenamento operacional temporário de movimentação.
saques_disponiveis:int = 3
saldo:float = 0.0
extrato:list = []

# Método que limpa a tela.
def limpa():
    os.system('cls')

# Método que faz uma pausa.
def pause():
    os.system('pause')

# Método para fazer um depósito.
def depositar():
    global saldo
    global extrato
    limpa()

    mensagem:str = """
    ╔═════════════════════════════════════════════════╗
    ║             Depósito em Conta Corrente          ║
    ╠═════════════════════════════════════════════════╣
    ║ Digite abaixo o valor de Depósito (R$):         ║
    ╠═════════════════════════════════════════════════╣
    ║ 0 - Cancela operação!                           ║
    ╚═════════════════════════════════════════════════╝
    """
    print(mensagem)

    try: #Tenta fazer o input de um valor, se for inválido o formato emite uma mensagem
        valor:float = float(input('R$ ▬► '))

        if valor >= 1.0: # Só aceita valores acima de 1.0, qualquer valor com 0, sai da operação de depósito.
            saldo = saldo + valor
            extrato.append(f"- Você fez um depósito de ▬► (+) R$ {valor:.2f}")
            aviso:str = """
            ╔═════════════════════════════════════════════════╗
            ║        Operação de depósito realizada!!!        ║
            ╚═════════════════════════════════════════════════╝
            """
            print(aviso)
            pause()

        else:
            aviso:str = """
            ╔═════════════════════════════════════════════════╗
            ║          Operação não permitida!!!              ║
            ╚═════════════════════════════════════════════════╝
            """
            print(aviso)
            pause()

    except ValueError:
        aviso:str = """
        ╔═════════════════════════════════════════════════╗
        ║           Digite um valor válido!!!             ║
        ╚═════════════════════════════════════════════════╝
        """
        print(aviso)
        pause()
        depositar()
    
# Método para fazer saques na conta.
def saques():
    global saldo
    global extrato
    global saques_disponiveis

    limpa()

    if saldo > 0.0 and saques_disponiveis > 0: # Se saldo for maior que zero e saques for maior que 0, permito a transação
        cabecalho:str = f"""
        ╔═════════════════════════════════════════════════╗
        ║                   Fazer Saque                   ║
        ╠═════════════════════════════════════════════════╣
        ║   ▬► Limite de saque por transação: R$ 500.00   ║
        ║   ▬► Limite total de saques por dia: 3          ║
        ╚═════════════════════════════════════════════════╝

           ▬► Saques permitidos: {saques_disponiveis}
           
        ╔═════════════════════════════════════════════════╗
        ║ 0 - Cancela operação!                           ║
        ╚═════════════════════════════════════════════════╝
        """
        print(cabecalho)

        try: #Tento fazer um saque se o valor estiver incorreto ou formato, emite um aviso.
            valor:float = float(input('- Digite o valor a sacar R$ ▬► '))

            if valor >= 1.0 and valor <= 500.0: #Verifico se o saldo é positivo 1.0 e menor que o limite de 500.0
                saldo = saldo - valor
                extrato.append(f"- Você fez um saque de ▬► (-) R$ {valor:.2f}")
                saques_disponiveis -= 1
                aviso:str = """
                ╔═════════════════════════════════════════════════╗
                ║         Operação de saque realizada!!!          ║
                ╚═════════════════════════════════════════════════╝
                """
                print(aviso)
                pause()

            elif valor > 500.0: # Qualquer tentativa de sacar um valor cima de 500.0 emito um aviso
                aviso:str = """
                ╔═════════════════════════════════════════════════╗
                ║ O valor de saque excede o limite por transação! ║
                ╚═════════════════════════════════════════════════╝
                """
                print(aviso)
                pause()

        except ValueError:
            aviso:str = """
            ╔═════════════════════════════════════════════════╗
            ║           Digite um valor válido !!!            ║
            ╚═════════════════════════════════════════════════╝
            """
            print(aviso)
            pause()

    else:
        if saques_disponiveis == 0: # Senão verifico se a quantidade permitida de saques zerou e amito um aviso.

            aviso:str = """
            ╔═════════════════════════════════════════════════╗
            ║    Limite diário de 3 saques está esgotado!!!   ║
            ╚═════════════════════════════════════════════════╝
            """
            print(aviso)
            pause()

        else: # Se o problema não for de limite de quantidade de saques esgotados é porque não há saldo o suficiente.   

            aviso:str = """
            ╔═════════════════════════════════════════════════╗
            ║                   Fazer Saque                   ║
            ╚═════════════════════════════════════════════════╝
                ▬► Limite de saque por transação: R$ 500.00
                ▬► Limite total de saques por dia: 3

            ╔═════════════════════════════════════════════════╗
            ║       Você não tem saldo para saques!!!         ║
            ╚═════════════════════════════════════════════════╝
            """
            print(aviso)
            pause()
        
# Método para verificar as movimentações bancárias.
def movimentacao():
    limpa()

    cabecalho:str = """
    ╔═════════════════════════════════════════════════╗
    ║                    Extrato                      ║
    ╠═════════════════════════════════════════════════╣
    ║            Histórico de Movimentação            ║
    ╚═════════════════════════════════════════════════╝
    """
    print(cabecalho)

    for dados in extrato: # Exibo a lista de todas as movimentações realizadas
        print(f"\t{dados}")

    # Exibe o saldo da conta a cada operação realizada.

    saldo_conta = f"""
    ═══════════════════════════════════════════════════
        Saldo em conta corrente ▬► (+) R$ {saldo:.2f}
    ═══════════════════════════════════════════════════
    """.upper()
    print(saldo_conta)
    pause()


menu = f"""
╔═════════════════════════════════════════════════╗
║ DIO    -   Sistema Eletrônico Bancário          ║
╠═════════════════════════════════════════════════╣
║                      MENU                       ║
║ 1 - DEPOSITO                                    ║
║ 2 - SAQUE                                       ║ 
║ 3 - EXTRATO                                     ║ 
╠═════════════════════════════════════════════════╣
║ 0 - SAIR                                        ║
╚═════════════════════════════════════════════════╝
"""

while True:
    limpa()
    print(menu)

    aviso = """
    ╔═════════════════════════════════════════════════╗
    ║               Opção inválida !!!                ║
    ╚═════════════════════════════════════════════════╝
    """
    # Menu de opções de transações do sistema bancário.
    try:
        opcao:int = int(input('▬► '))

        if opcao == 0:
            limpa()
            exit(0)

        if opcao == 1:
            depositar()

        if opcao == 2:
            saques()

        if opcao == 3:
            movimentacao()

        if opcao > 3: # Se entrar qualquer valor acima das opções, emito um aviso.
            print(aviso)
            pause()

    except ValueError:
        print(aviso) # Se a opção for errada ou forma incorreta, emito um aviso.
        pause()
