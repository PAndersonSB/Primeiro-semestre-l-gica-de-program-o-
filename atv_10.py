def validação(lista):
    parenteses_f = []
    parenteses_a = []
    colchete_f = []
    colchete_a = []
    for simbolo in lista:
        if simbolo == '(':
            parenteses_a.append('(')
        elif simbolo == ')':
            parenteses_f.append(')')
        elif simbolo == '[':
            colchete_a.append('[')
        elif simbolo == ']':
            colchete_f.append(']')

        if len(parenteses_f) > len(parenteses_a) or len(colchete_f) > len(colchete_a):#como é salvo sempre que acha um ( ou ) , é considerado invalido se tiver mais parenteses fechando
            return "expressão invalida"
            break
    if len(parenteses_f) != len(parenteses_a) or len(colchete_f) != len(colchete_a):#se o numero de de parenteses fechando n for igual aos parenteses abrindo é considerado invalido
        return "expressão invalida"
    else:
        return "expressão valida"

def vetor(lista):
    qtde = len(lista)
    i = 0
    vetor = ['x'] * 50

    while i < qtde:
        armazen = ''
        while i < qtde and lista[i].isnumeric() or i < qtde and lista[i] == '.':
            indicex = vetor.index('x')
            armazen = armazen + lista[i]

            i += 1
        indicex = vetor.index('x')
        vetor[indicex] = armazen
        armazen = ''

        if i < qtde :
            indicex = vetor.index('x')
            armazen = armazen + lista[i]

            vetor[indicex] = armazen

            i += 1

    return vetor


def quatro_operaçoes (lista):
    lista = calcula_prioridade(lista, "*")
    lista = calcula_prioridade(lista, "/")
    lista = calcula_prioridade(lista, "-")
    lista = calcula_prioridade(lista, "+")
    return lista

def calcula_operacao_basica(numero1, op, numero2):
    if op == "+":
        resultado = numero1 + numero2
    elif op == "-":
        resultado = numero1 - numero2
    elif op == "*":
        resultado = numero1 * numero2
    elif op == "/":
        resultado = numero1 / numero2
    return resultado

def calcula_prioridade(lista, operador):
    qtde = len(lista)
    i = 0
    lista_aux = []
    
    while i < qtde:
        while i < qtde and lista[i] != operador:
            lista_aux.append(lista[i])
            i += 1
    
        if i < qtde:
            aux = calcula_operacao_basica(float(lista_aux[-1]), operador, float(lista[i+1]))
            lista_aux[-1] = aux
            i += 1
        
        i +=1
    
    return lista_aux

def calcula_dentro_de_parenteses(lista, simbolo1, simbolo2):
    qtde = len(lista)
    i = 0
    lista_aux = []
    lista_aux2 = []

    while i < qtde:
        while i < qtde and lista[i] != simbolo1:
            lista_aux.append(lista[i])
            i += 1

        i += 1

        while i < qtde and lista[i] != simbolo2:
            lista_aux2.append(lista[i])
            i += 1

        #calculo da lista auxiliar 2 e adicinando ela na lista1
        aux = quatro_operaçoes (lista_aux2)
        aux = str(aux).strip('[]')
        lista_aux.append(aux)
        i += 1
        lista_aux2.clear()

    lista_aux.pop()

    return lista_aux

def calcula_dentro_de_colchetes(lista, simbolo1, simbolo2):
    qtde = len(lista)
    i = 0
    lista_aux = []
    lista_aux2 = []

    while i < qtde:
        while i < qtde and lista[i] != simbolo1:
            lista_aux.append(lista[i])
            i += 1

        i += 1

        while i < qtde and lista[i] != simbolo2:
            lista_aux2.append(lista[i])
            i += 1

        #calculo da lista auxiliar 2 e adicinando ela na lista1
        aux = quatro_operaçoes (lista_aux2)
        aux = str(aux).strip('[]')
        lista_aux.append(aux)
        i += 1
        lista_aux2.clear()

    lista_aux.pop()
    return lista_aux

def calcula_dentro_de_chaves(lista, simbolo1, simbolo2):
    qtde = len(lista)
    i = 0
    lista_aux = []
    lista_aux2 = []

    while i < qtde:
        while i < qtde and lista[i] != simbolo1:
            lista_aux.append(lista[i])
            i += 1

        i += 1

        while i < qtde and lista[i] != simbolo2:
            lista_aux2.append(lista[i])
            i += 1

        #calculo da lista auxiliar 2 e adicinando ela na lista1
        aux = quatro_operaçoes (lista_aux2)
        aux = str(aux).strip('[]')
        lista_aux.append(aux)
        i += 1
        lista_aux2.clear()

    lista_aux.pop()
    return lista_aux

#"2+(3*5)+[2*(3-6/2+9)/3]-8/2"
lista = "-2+(3.8*5)+[2.5*(3-6/2+9)/3]-82/2"
print(lista)

print(validação(lista))#função validação

lista = vetor(lista) #nova função que usa vetor
print(lista)

#tratamento da lista

while lista.count('') != 0: #tirando espaços em brancos
    indice_espaço = lista.index('')
    lista.pop(indice_espaço)

if lista[0] == '-':  # se o primeiro indice do vetor for "-" ele transforma em um numero negativo
    del lista[0]
    lista[0] = '-' + lista[0]

while lista[-1] == 'x':  # tira todos os x do Vetor
    del lista[-1]

print(lista)


lista = calcula_dentro_de_parenteses(lista, "(", ")")
print("lista resolvendo os () ", lista)

lista = calcula_dentro_de_colchetes(lista, "[", "]")
print("lista resolvendo os colchetes", lista)


lista = quatro_operaçoes(lista)

print("lista totalmente resolvida ", lista)
