matriz = [[17, "Jair Bolsonaro", 0], [13, "Fernando Haddad", 0], [18, "Marina Silva", 0], [0, "votos nulos", 0]]
confirmVoto = True
def candidatos ():
    print(f'número de candidato: {matriz[0][0]}, candidato: {matriz[0][1]}')
    print(f'número de candidato: {matriz[1][0]}, candidato: {matriz[1][1]}')
    print(f'número de candidato: {matriz[2][0]}, candidato: {matriz[2][1]}')

while matriz[0][2] + matriz[1][2] + matriz[2][2] + matriz[3][2] < 10: #enquanto menor que 10 votos
    candidatos()

    while confirmVoto:
        voto = int(input('\ninsira o número do candidato: '))
        confirm = int(input('\ndigite 1 para confirmar seu voto: '))
        if confirm != 1:
            print('\nvoto cancelado')
        else:
            print('\nvoto confirmado')
            confirmVoto = False

    print('\nseu voto é ', voto, '\n')
    confirmVoto = True

    if voto == 17 and matriz[0][2] == 3: #desvio , se o voto for para o bolsonaro e ele tiver um total de 3 votos , os votos são anulados
        matriz[3][2] = matriz[3][2] + 1

    elif voto == 17:
        matriz[0][2] = matriz[0][2] + 1

    elif voto == 13:
        matriz[1][2] = matriz[1][2] + 1

    elif voto == 18:
        matriz[2][2] = matriz[2][2] + 1

    else:
        matriz[3][2] = matriz[3][2] + 1

print(matriz)

print(matriz[0][0], matriz[0][1], f'com um total de: {matriz[0][2]} votos\n')
print(matriz[1][0], matriz[1][1], f'com um total de: {matriz[1][2]} votos\n')
print(matriz[2][0], matriz[2][1], f'com um total de: {matriz[2][2]} votos\n')
print(f'um total de {matriz[3][2]} votos nulos')

arquivo = open("resultado_dos_votos.txt", "w")

arquivo.write(f'{str(matriz)}\n')

#primeiro print
#arquivo.write(str(matriz[0][0]))
#arquivo.write(str(matriz[0][1]))
arquivo.write(f'\n{str(matriz[0][0])} {str(matriz[0][1])} com um total de: {str(matriz[0][2])} votos\n')

#segundo print
#arquivo.write(str(matriz[1][0]))
#arquivo.write(str(matriz[1][1]))
arquivo.write(f'\n{str(matriz[1][0])} {str(matriz[1][1])} com um total de: {str(matriz[1][2])} votos\n')

#terceiro print
#arquivo.write(str(matriz[2][0]))
#arquivo.write(str(matriz[2][1]))
arquivo.write(f'\n{str(matriz[2][0])} {str(matriz[2][1])} com um total de: {str(matriz[2][2])} votos\n')

#quarto print
arquivo.write(f'\num total de {str(matriz[3][2])} votos nulos')

arquivo.close()