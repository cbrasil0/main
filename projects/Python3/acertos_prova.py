# Verificação da quantidade de acertos de prova do tipo múltipla escolha. Python 3

# dados de entrada: número total de questões; respostas de cada questão; gabarito de cada questão
# solução: realizar a comparação entre as respostas e o gabarito, adicionando um contador para cada acerto
# dados de saída: número total de acertos, percentual de acertos

num_questoes = int(input("Número total de questões: ")) #entrada do número total de questões
respostas = input("Respostas (separadas por um espaço ex. C A E B B...): ").split(" ") #entrada das respostas marcadas
gabarito = input("Gabarito (ex. C A A A E...): ").split(" ") #entrada das respostas do gabarito

#converter as respostas em uma lista com cada marcação sendo um elemento
def convert_r(respostas):
    lista_r = list(respostas)
    return lista_r

#converter o gabarito em uma lista com cada resposta sendo um elemento
def convert_g(gabarito):
    lista_g = list(gabarito)
    return lista_g

lista_r = convert_r(respostas) #conversão respostas
lista_g = convert_g(gabarito) #conversão gabarito

acertos = 0
i = 0
#verificando acertos por comparação entre as respostas e o gabarito
for i in range(num_questoes):
    if lista_r[i] == lista_g[i]:
        acertos += 1
    #else:
        #acertos-= 1 #para provas em que cada erro subtrai um ponto

print("Você acertou ",acertos," de um total de ",num_questoes," questões.",sep="")
aproveitamento = float(acertos/num_questoes) * 100
print("Isso representa um total de ",f"{aproveitamento:.2f}","% de aproveitamento.", sep="")
