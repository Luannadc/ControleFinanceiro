### Controle de Gastos Financeiros Pessoais
# Este programa tem como objetivo ajudar o usuário a controlar seus gastos financeiros pessoais.
# Inicializa as listas para armazenar receitas, despesas e investimentos
receitas = []
despesas = []
investimentos = []
categorias = ["Alimentação", "Transporte", "Investimento", "Saúde", "Educação", "Lazer", "Casa", "Outros"]

# Inicializa as variáveis para armazenar o total de receitas, despesas e investimentos
total_receitas = 0
total_despesas = 0
total_investimentos = 0
# Inicializa a variável para armazenar o saldo
saldo = 0
# Função para registrar uma receita
def registrar_receita():
    global total_receitas
    global saldo
    descricao = input("Descrição da receita: ")
    valor = float(input("Valor da receita: "))
    data = input("Data da receita (dd/mm/aaaa): ")
    receitas.append({"descricao": descricao, "valor": valor, "data": data})
    total_receitas += valor
    saldo += valor
    print("Receita registrada com sucesso!")
# Função para registrar uma despesa
def registrar_despesa():
    global categorias
    global total_despesas
    global saldo
    descricao = input("Descrição da despesa:")
    valor = float(input("Valor da despesa: "))
    data = input("Data da despesa (dd/mm/aaaa):")
    print("Categoria da despesa: ")
    for i, categoria in enumerate(categorias):
        print(f"{i+1}. {categoria}")
    escolha = input("Escolha o numero da categoria:")
    if escolha.isdigit() and 1 <= int(escolha) <= len(categorias):
        categoria = categorias[int(escolha) - 1]
    else: 
        categoria = escolha
    if categoria not in categorias:
        categorias.append(categoria)
        print(f"'{valor}' adicionado em '{categoria}'")
        # Se a categoria for "Outros", pergunta se o usuário deseja adicionar uma nova categoria
        if categoria == "Outros":
            print("Deseja adicionar uma nova categoria? (s/n)")
            resposta = input()
            if resposta == "s":
                nova_categoria = input("Digite o nome da nova categoria: ")
                categorias.append(nova_categoria)
                print(f"Categoria '{nova_categoria}' adicionada com sucesso!")
            else:
                print("Categoria não adicionada.")
    despesas.append({"descricao": descricao, "categoria": categoria, "valor": valor, "data": data})
    total_despesas += valor
    saldo -= valor
    print("Despesa registrada com sucesso!")    
# Função para registrar um investimento
def registrar_investimento():
    global total_investimentos
    global saldo
    descricao = input("Descrição do investimento: ")
    valor = float(input("Valor do investimento: "))
    categoria = "Investimento"
    data = input("Data do investimento (dd/mm/aaaa): ")
    investimentos.append({"descricao": descricao, "valor": valor, "data": data})
    total_investimentos += valor
    saldo -= valor
    print("Investimento registrado com sucesso!")
# Função para listar as transações
from datetime import datetime
def listar_transacoes():
  
    todas_transacoes = []
    for receita in receitas:
        todas_transacoes.append({"tipo": "Receita", **receita})
    for despesa in despesas:
        todas_transacoes.append({"tipo": "Despesa", **despesa})
    for investimento in investimentos:
        todas_transacoes.append({"tipo": "Investimento", **investimento})

    # Ordena as transações da mais recente para a mais antiga
    todas_transacoes.sort(key=lambda t: datetime.strptime(t['data'], "%d/%m/%Y"), reverse=True)

    print("\n=== Transações Realizadas ===")
    for transacao in todas_transacoes:
        print(f"{transacao['data']} | {transacao['tipo']:<12} | {transacao['descricao']:<20} | R$ {transacao['valor']:.2f}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# Função para buscar transações por categoria
def buscar_categoria():
    categoria = input("Digite a categoria que deseja buscar: ")
    transacoes_encontradas = []
    for despesa in despesas:
        if despesa["categoria"] == categoria:
            transacoes_encontradas.append(despesa)
    if transacoes_encontradas:
        print(f"\n=== Transações na categoria '{categoria}' ===")
        for transacao in transacoes_encontradas:
            print(f"{transacao['data']} | Despesa | {transacao['descricao']:<20} | R$ {transacao['valor']:.2f}")
    else:
        print(f"Nenhuma transação encontrada na categoria '{categoria}'.")
# Função para simular o rendimento de um investimento
def simular_rendimento():
    valor_investido = float(input("Valor investido: "))
    taxa_juros = float(input("Taxa de juros (% ao ano): "))
    tempo = int(input("Tempo (em anos): "))
    rendimento = valor_investido * ((1 + (taxa_juros / 100)) ** tempo)
    print(f"Rendimento após {tempo} anos: R$ {rendimento:.2f}")
# Função para exibir o resumo financeiro
def resumo_financeiro():
    print("\n=== Resumo Financeiro ===")
    print(f"Total de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"Total de Investimentos: R$ {total_investimentos:.2f}")
    print(f"Saldo Atual: R$ {saldo:.2f}")
    # Porcentagem de cada categoria
    print("\n=== Porcentagem de cada categoria ===")
    total_despesas_categoria = sum(despesa["valor"] for despesa in despesas)
    for categoria in categorias:
        total_categoria = sum(despesa["valor"] for despesa in despesas if despesa["categoria"] == categoria)
        porcentagem_categoria = (total_categoria / total_despesas_categoria) * 100 if total_despesas_categoria > 0 else 0
        print(f"{categoria}: {porcentagem_categoria:.2f}%")
# Loop principal do programa

while True:
    print("\n=== Controle de Gastos Financeiros Pessoais ===")
    print("1. Registrar Receita")
    print("2. Registrar Despesa")
    print("3. Registrar Investimento")
    print("4. Listar Transações")
    print("5. Buscar Transações por Categoria")
    print("6. Simular Rendimento de Investimento")
    print("7. Resumo Financeiro")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_receita()
    elif opcao == "2":
        registrar_despesa()
    elif opcao == "3":
        registrar_investimento()
    elif opcao == "4":
        listar_transacoes()
    elif opcao == "5":
        buscar_categoria()
    elif opcao == "6":
        simular_rendimento()
    elif opcao == "7":
        resumo_financeiro()
    elif opcao == "8":
        break
    else:
        print("Opção inválida! Tente novamente.")
