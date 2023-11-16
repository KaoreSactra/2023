# Import's
import requests
import time
import os
from tkinter import *
from bs4 import BeautifulSoup

# Urls
url_opinion = 'https://www.gov.br/participamaisbrasil/consulta-publica-conitec-sectics-n-36-2023-opiniao-palivizumabe'
url_technical = 'https://www.gov.br/participamaisbrasil/consulta-publica-conitec-sectics-n-36-2023-tecnico-cientifico-palivizumabe'

# headers (my user agent)
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

# Limpar Terminal
os.system('cls')

# main - Buscar infos:
def buscar_consutas():
        # campo de busca 1
        site1 = requests.get(url_opinion, headers=headers)
        soup1 = BeautifulSoup(site1.content, 'html.parser')
        box1 = soup1.find_all('div', class_='column col-md-12')[0]
        contributions1 = box1.find_all('p')[5].get_text()
        cont1 = contributions1.replace("Contribuições Recebidas:", "")
        ct1 = cont1.strip()

        # campo de busca 2
        site2 = requests.get(url_technical, headers=headers)
        soup2 = BeautifulSoup(site2.content, 'html.parser')
        box2 = soup2.find_all('div', class_='column col-md-12')[0]
        contributions2 = box2.find_all('p')[5].get_text()
        cont2 = contributions2.replace("Contribuições Recebidas:", "")
        ct2 = cont2.strip()

        # imprimindo informações
        print('---------------------')
        print(f'Opinião = {ct1}')
        print(f'Técnico = {ct2}')
        print('---------------------')

        b2['text'] = ct1
        b4['text'] = ct2

# Janela
janela = Tk() # Definindo janela

# Titulo
janela.title('Consulta Pública')
janela.geometry('260x210')

# dentro da janela
subtitulo = ['Opinião', 'Técnico']
contibuicoes = 'Contribuições Recebidas:'

a1 = Label(janela, text=subtitulo[0])
a1.grid(column=0, row=0, padx=10, pady=10)

a2 = Label(janela, text=contibuicoes)
a2.grid(column=0, row=1, padx=10, pady=10)

a3 = Label(janela, text=subtitulo[1])
a3.grid(column=0, row=2, padx=10, pady=10)

a4 = Label(janela, text=contibuicoes)
a4.grid(column=0, row=3, padx=10, pady=10)

b2 = Label(janela, text='Sem dados')
b2.grid(column=1, row=1, padx=10, pady=10)

b4 = Label(janela, text='Sem dados')
b4.grid(column=1, row=3, padx=10, pady=10)

b5 = Button(janela, text='Atualizar', command=buscar_consutas)
b5.grid(column=1, row=4, padx=10, pady=10)

# fazer a janela continuar sendo exibida
janela.mainloop()