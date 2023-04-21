meses_sistema = ["jan2022","fev2022","mar2022","abr2022","mai2022","jun2022","jul2022","ago2022","set2022","out2022","nov2022","dez2022","jan2021","fev2021","mar2021","abr2021","mai2021","jun2021","jul2021","ago2021","set2021","out2021","nov2021","dez2021","jan2020","fev2020","mar2020","abr2020","mai2020","jun2020","jul2020","ago2020","set2020","out2020","nov2020","dez2020","jan2019","fev2019","mar2019","abr2019","mai2019","jun2019","jul2019","ago2019","set2019","out2019","nov2019","dez2019","jan2018","fev2018","mar2018","abr2018","mai2018","jun2018","jul2018","ago2018","set2018","out2018","nov2018","dez2018","jan2017","fev2017","mar2017","abr2017","mai2017","jun2017","jul2017","ago2017","set2017","out2017","nov2017","dez2017"]

print(len(meses_sistema))

#biblioteca para acessar as pastas/arquivos no seu computador
import os

arquivosExtraidos = []

#pegar os arquivos que estão na pasta"Arquivos" e vai adicionar na variavel arquivos extraidos
def pegarArquivosPasta(pasta):
    #listar os arquivos que estão na pasta
    listaArquivos = os.listdir(pasta)

    #se tiver .txt e vendas no nome do arquivo entao vou pegar o nome do mes
    for arquivo in listaArquivos:
        if ".txt" in arquivo and "Vendas" in arquivo:
            #pegar o nome do mes
            nomeMes = arquivo.split()[-1].replace(".txt", "")
            arquivosExtraidos.append(nomeMes)
        elif ".txt" not in arquivo: #se é uma pasta
            pegarArquivosPasta(f'{pasta}/{arquivo}') #dentro da pasta vai pegar os arquivos

print(arquivosExtraidos)

pegarArquivosPasta("Arquivos")

#verificar se no mes_sistema falta algum arquivo que foi selecionado com a função pegarArquivosPasta
for mes in meses_sistema:
    if mes not in arquivosExtraidos:
        print(mes)



#=============== ALGUMAS ANOTAÇÕES ===============#
#nomeMes = arquivo.split()[-1].replace(".txt", "")
#split() - quando vazio vai separar pelos espaços
#  - 'Compras - agosto2022' -> ['Compras', '-', 'agosto2022']
#
#[-1] -> pega o ultimo item
#
#replace - trocar ".txt" por vazio no nome que for aparecer