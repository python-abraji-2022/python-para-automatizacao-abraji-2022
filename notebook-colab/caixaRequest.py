import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/'

numeroConcursoEsperado = 2508


def verificaConcurso(concursoAnterior, numeroConcursoEsperado):
    print(
        f'--------->>>> Concurso Anterior {concursoAnterior} Proximo Concurso {numeroConcursoEsperado}')
    return numeroConcursoEsperado == concursoAnterior


def imprimeInformacoes(resultados):
    print('---'*30)
    print('--'*10, end='')
    print('Dados do Concurso Atual', end='')
    print('--'*10)
    print('---'*30)
    print(premiacao['listaDezenas'])


contador = 0
while True:
    resp = requests.get(url, verify=False)
    soup = BeautifulSoup(resp.content, 'html5lib')
    body = soup.find('body').text
    premiacao = json.loads(body)
    if verificaConcurso(premiacao['numero'], numeroConcursoEsperado) or contador == 10:
        imprimeInformacoes(premiacao)
        break
    else:
        contador += 1
        print(f'Tentativa de número {contador}')
        time.sleep(2)
