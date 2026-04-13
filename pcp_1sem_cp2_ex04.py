# Função para calcular horas extras
def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = salario_base * 0.015
    return valor_hora_extra * horas

# Função para calcular descontos por faltas
def calcular_descontos_faltas(salario_base, faltas):
    desconto_por_falta = salario_base * 0.02
    return desconto_por_falta * faltas

# Função para calcular bônus
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

# Programa principal
nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: "))
horas_extras = float(input("Horas extras: "))
faltas = int(input("Faltas no mês: "))
recebeu_bonus = input("Recebeu bônus? (s/n): ")

# Cálculos
valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base
acrescimos = valor_horas_extras + valor_bonus
descontos = valor_descontos
salario_final = salario_bruto + acrescimos - descontos

# Saída
print("\n--- RESUMO ---")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Acréscimos: R$ {acrescimos:.2f}")
print(f"Descontos: R$ {descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")