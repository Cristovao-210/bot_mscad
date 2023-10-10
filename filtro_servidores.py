import pandas as pd

# Carregando dados
servidores = pd.read_csv(f'listaServidores.csv', sep=",", encoding='latin-1')

# filtrando e gerando arquivo de servidores do HUB
with open('servidores257.csv', 'w', encoding='latin-1') as hub:
    hub.write(f'SIAPE,NOME,CATEGORIA,UNIDADE DE EXERCÍCIO\n')
    for ind, uni in enumerate(servidores['UNIDADE DE EXERCÍCIO']):
        if uni == "HOSPITAL DA UNIVERSIDADE DE BRASILIA" or uni == "HOSP-HOSPITAL UNIVERSITÁRIO DE BRASÍLIA":
            hub.write(f"{servidores['SIAPE'][ind]},{servidores['NOME'][ind]},{servidores['CATEGORIA'][ind]},{servidores['UNIDADE DE EXERCÍCIO'][ind]}\n")

# filtrando e gerando arquivo de servidores da UNB
with open('servidores606.csv', 'w', encoding='latin-1') as unb:
    unb.write(f'SIAPE,NOME,CATEGORIA,UNIDADE DE EXERCÍCIO\n')
    for ind, uni in enumerate(servidores['UNIDADE DE EXERCÍCIO']):
        if uni == "HOSPITAL DA UNIVERSIDADE DE BRASILIA" or uni == "HOSP-HOSPITAL UNIVERSITÁRIO DE BRASÍLIA":
            continue
        else:
            unb.write(f"{servidores['SIAPE'][ind]},{servidores['NOME'][ind]},{servidores['CATEGORIA'][ind]},{str(servidores['UNIDADE DE EXERCÍCIO'][ind]).replace(',','')}\n")
    
