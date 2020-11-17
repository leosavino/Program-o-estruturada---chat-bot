import pandas as pd


linha = 1
true = 1
resposta_certa = 1

texto = pd.read_csv("teste.csv",sep=';',index_col="ID")

while true == 1:
    row = texto.loc[linha]
    if row["Pergunta"] == "NÓ FOLHA":
        print(row["A"])
        break
    else:
        print(row["Pergunta"])
        print("Digite 1 para verdadeiro e 2 para falso")
        resposta = int(input())
        while resposta != 1 and resposta != 2:
            print("Resposta invalida, digite novamente \n1 para verdadeiro e 2 para falso")
            resposta = int(input())

    if resposta == 1:
        linha = int(row["Nó A"])
        resposta == 0
    elif resposta == 2:
        linha = int(row["Nó B"])
        resposta == 0
