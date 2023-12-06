import re
from collections import Counter

texto = open('folha8.OUT.txt', 'r',encoding='utf-8').read()

#Calcular quantas publicações

def publis(texto):
    dates = texto.count('#DATE')
    print(f'O número de publicações na Folha 8 são: {dates}')

publis(texto)

#Extrair lista de # e respetivo numero de ocorrências

def cardinal(texto):
    linhas = texto.split('\n')
    oco = {}
    for linha in linhas:
            if linha.startswith('#DATE'):
                if linha in oco:
                    oco[linha] += 1
                else:
                    oco[linha] = 1
    return oco

contagem = cardinal(texto)

with open('lista_de_pubs.txt', 'w', encoding='utf-8') as f:
      for linha, ocorrencias in contagem.items():
            f.write(f'{linha}: {ocorrencias} publicações\n')


#Que gama de datas estão incluídas no ficheiro


def datas_numeros(texto):
    texto_sem_quebras = texto.replace('\n', '')
    padrao = (r'\b\d{1,2}/\b\d{1,2}/\b\d{2,4}\b|\b\d{1,2}-\b\d{1,2}-\b\d{2,4}\b|\b\d{1,2}/b/\b\d{1,2}/\b\d{1,2}')
    datas_numeros = re.findall(padrao, texto_sem_quebras)
    oco = {}
    for data in datas_numeros:
        if data in oco:
              oco[data] += 1
        else:
            oco [data] = 1
    return oco

def datas_extenso(texto):
    texto_sem_quebras = texto.replace('\n', '')
    padrao_dois = (r'\b\d{1,2}\b\s\bde\b\s\b\w*\b\s\bde\b\sd{2,4}|\b\d{1,2}\b\s\bde\b\s\w*\s(?:\bde\b\s\d{2,4}\b)?')
    datas_por_extenso = re.findall(padrao_dois, texto_sem_quebras)
    oco = {}
    for data in datas_por_extenso:
        if data in oco:
              oco[data] += 1
        else:
            oco [data] = 1
    return oco

contagem_numeros = datas_numeros(texto)
contagem_extenso = datas_extenso(texto)

with open('gama_de_datas.txt', 'a', encoding='utf-8') as f:
    for data_extenso, ocorrencias_extenso in contagem_extenso.items():
        f.write(f'Datas por extenso: {data_extenso}: {ocorrencias_extenso} ocorrências\n')

with open('gama_de_datas.txt', 'a', encoding='utf-8') as f:
    for data_numeros, ocorrencias_numeros in contagem_numeros.items():
        f.write(f'Datas com barra ou travessão: {data_numeros}: {ocorrencias_numeros} ocorrências\n')


#EXERCÍCIO LIVRE - Saber quais são as palavras mais utilizadas, de forma a permitir saber qual é o tema mais comum ao longo da Folha

def contar_palavras_sem_stopwords(texto, stopwords):
    palavras = texto.lower().split()
    contagem = {}
    for palavra in palavras:
        if palavra not in stopwords:
            contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

stopwords_exemplo = {"é", 'a', 'o', 'que', 'e', 'do', "um", "de", "este", "como", 'da', 'em', 'para', 'os', 'dos', 'com', 'no', 'não', 'na', 'uma', 'por', 'as', 'se', 'ao', 'à', 'das', 'mais', 'ser', 'ou', 'foi', '–', 'pelo', 'mas', 'sua', 'pela', 'são', 'nos', 'tem', 'está', 'também', 'seu', 'entre', 'aos', 'ainda', 'sobre', 'já'}

contagem_palavras = contar_palavras_sem_stopwords(texto, stopwords_exemplo)

palavras_comuns = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)[:5]

print(f'As palavas mais comuns na Folha 8, excluindo stopwords, são: {palavras_comuns}')