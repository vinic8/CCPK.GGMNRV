# Função para verificar se o cliente pode ser aprovado
def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= (renda * 20):
        return True
    return False

# Função para definir a taxa de juros com base no número de parcelas
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05  # 5% ao mês
    elif parcelas <= 12:
        return 0.08  # 8% ao mês
    else:
        return 0.10  # 10% ao mês

# Função para calcular o valor da parcela
def calcular_parcela(valor, taxa, parcelas):
    i = taxa  # Taxa de juros mensal
    n = parcelas  # Número de parcelas
    pmt = valor * (i * (1 + i)**n) / ((1 + i)**n - 1)
    return pmt

# Função para calcular o valor total pago ao longo do financiamento
def calcular_total(parcela, parcelas):
    return parcela * parcelas

# Função para calcular o valor dos juros pagos
def calcular_juros(total, valor):
    return total - valor

# Solicitar os dados do cliente
nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: "))
valor = float(input("Digite o valor desejado do empréstimo: "))
parcelas = int(input("Digite o número de parcelas (3 a 24): "))

if not pode_aprovar(idade, renda, valor):
    print("Empréstimo negado: O cliente não atende aos requisitos de idade ou valor.")
else:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total_pago = calcular_total(parcela, parcelas)
    juros = calcular_juros(total_pago, valor)

    # Exibir as informações do financiamento
    print("\nEmpréstimo aprovado!")
    print(f"Nome do cliente: {nome}")
    print(f"Valor financiado: R${valor:.2f}")
    print(f"Taxa de juros aplicada: {taxa * 100:.2f}% ao mês")
    print(f"Valor da parcela: R${parcela:.2f}")
    print(f"Valor total pago: R${total_pago:.2f}")
    print(f"Total de juros pagos: R${juros:.2f}")