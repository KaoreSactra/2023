#Import
import requests
from bs4 import BeautifulSoup

#Urls
url_opinion = 'https://www.gov.br/participamaisbrasil/consulta-publica-conitec-sectics-n-36-2023-opiniao-palivizumabe'
url_technical = 'https://www.gov.br/participamaisbrasil/consulta-publica-conitec-sectics-n-36-2023-tecnico-cientifico-palivizumabe'

#headers (my user agent)
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

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
print(f'Opinião {contributions1}.')
print(f'Técnico {contributions2}.')