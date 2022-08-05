from attr import attr
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def imprimeInformacoes(resultados):
    print('--'*30)
    print('--'*10, end='')
    print('Dados do Concurso Atual', end='')
    print('--'*10)
    print('--'*30)
    bolas = resultados.find_all('li', attrs={'class': 'ng-binding ng-scope'})

    for ball in bolas:
        print(f'{ball.text}', end=' - ')

    premiacoes = resultados.find(
        'div', attrs={'class': 'related-box gray-text no-margin'})

    print(premiacoes.find_all('strong')[0].text)
    print(premiacoes.find_all('span', attrs={
          'class': 'ng-binding ng-hide'})[0].text)
    print(premiacoes.find_all('strong')[1].text)
    print(premiacoes.find_all('span', attrs={
          'class': 'ng-binding ng-hide'})[1].text)
    print(premiacoes.find_all('strong')[2].text)
    print(premiacoes.find_all('span', attrs={
          'class': 'ng-binding ng-hide'})[2].text)


def verificaConcurso(resultadoAnterior, numeroConcursoEsperado):
    numeroAtual = resultadoAnterior.find('h2').text.split()
    print(
        f'--------->>>> Concurso Anterior {numeroAtual[2]} Proximo Concurso {numeroConcursoEsperado}')
    return numeroConcursoEsperado == numeroAtual[2]


chromedriver = 'notebook-colab/driver/chromedriver'

option = Options()
option.headless = True

driver = webdriver.Chrome(chromedriver, options=option)

url = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"
driver.get(url)
time.sleep(3)
numeroConcursoEsperado = '2508'

while True:
    print('Dentro do Loop')
    html = driver.page_source

    conteudo = BeautifulSoup(html, 'lxml')
    resultados = conteudo.find('div', attrs={'id': 'conteudoresultado'})

    if verificaConcurso(resultados, numeroConcursoEsperado):
        imprimeInformacoes(resultados)
        break
    else:
        driver.refresh()
        time.sleep(3)

driver.close()
