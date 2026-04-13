estado = float(input('qual é o estado da carga do caminhão:'))
peso = float(input('qual é o peso da carga do caminhão em toneladas:'))
codigo = float(input('qual é o código da carga entre 10 a 40:'))

peso_kg = peso * 1000
print(f'o peso em kilogramas é:{peso_kg}')

preco = 0
imposto = 0

if codigo >= 10 and codigo <= 20:
    preco = peso_kg * 100
    print(f"O preço é:{preco}")
elif codigo >= 21 and codigo <= 30:
    preco = peso_kg * 250
    print(f"O preço é:{preco}")
elif codigo >= 31 and codigo <= 40:
    preco = peso_kg * 340
    print(f"O preço é:{preco}")
else:
    print("erro")

if estado == 1:
    imposto = preco * 0.35
    print(f'O imposto é:{imposto}')
elif estado == 2:
    imposto = preco * 0.25
    print(f'O imposto é:{imposto}')
elif estado == 3:
    imposto = preco * 0.15
    print(f'O imposto é:{imposto}')
elif estado == 4:
    imposto = preco * 0.05
    print(f'O imposto é:{imposto}')
elif estado == 5:
    print('isento de imposto')

preco_total = preco + imposto
print(f'o preço total é igual a = R${preco_total}')