#Import
import requests
import openpyxl as pyxl
from openpyxl.styles import numbers
from bs4 import BeautifulSoup

#Urls
url_opinion = 'https://www.gov.br/participamaisbrasil/consulta-publica-conitec-sectics-n-36-2023-opiniao-palivizumabe'
url_technical = 'https://www.gov.br/participamaisbrasil/consulta-publica-conitec-sectics-n-36-2023-tecnico-cientifico-palivizumabe'

#headers (my user agent)
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

#print
print('Buscando informações:')

#campo de busca 1
site1 = requests.get(url_opinion, headers=headers)
soup1 = BeautifulSoup(site1.content, 'html.parser')
box1 = soup1.find_all('div', class_='column col-md-12')[0]
contributions1 = box1.find_all('p')[5].get_text()

#campo de busca 2
site2 = requests.get(url_technical, headers=headers)
soup2 = BeautifulSoup(site2.content, 'html.parser')
box2 = soup2.find_all('div', class_='column col-md-12')[0]
contributions2 = box2.find_all('p')[5].get_text()

#prints
print('.....................')
print(f'Opinião = {contributions1}')
print(f'Técnico = {contributions2}')
print('.....................')

#formatando a resposta
cont1 = contributions1.replace("Contribuições Recebidas:", "")
ct1 = cont1.strip()
cont2 = contributions2.replace("Contribuições Recebidas:", "")
ct2 = cont2.strip()

#prints
print('.....................')
print(f'{ct1}')
print(f'{ct2}')
print('.....................')

#carregando a planilha
wb = pyxl.load_workbook('Tracking.xlsx')

#selecionando a pasta
sheet1 = wb['Sheet1']

#adicionando os valores
sheet1['b2'].value = f'{ct1}'
sheet1['b2'].number_format = numbers.FORMAT_GENERAL

sheet1['c2'].value = f'{ct2}'
sheet1['c2'].number_format = numbers.FORMAT_NUMBER

wb.save('Tracking.xlsx')