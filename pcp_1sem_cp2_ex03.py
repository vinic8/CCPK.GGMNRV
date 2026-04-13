#Notas
CP1 = float(input("Digite a nota da CP1 (0 a 10): "))
CP2 = float(input("Digite a nota da CP2 (0 a 10): "))
CP3 = float(input("Digite a nota da CP3 (0 a 10): "))
SP1 = float(input("Digite a nota da SP1 (0 a 10): "))
SP2 = float(input("Digite a nota da SP2 (0 a 10): "))
GS = float(input("Digite a nota da GS (0 a 10): "))

#Calculos
menor_cp = min(CP1, CP2, CP3)
soma_cp = CP1 + CP2 + CP3 - menor_cp
media = (soma_cp + SP1 + SP2) / 4
media_final = (media * 0.4) + (GS * 0.6)
media_peso = media_final * 0.4

#Output
print("Menor checkpoint desconsiderado:", menor_cp)
print("Média final:", media_final)
print(f"Média semestral (com peso de 40%): {media_peso:.2f}") #maximo 4 pontos na media total do ano