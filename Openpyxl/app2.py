import openpyxl

#carregando arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')
#selecionando a página
frutas_pages = book['Frutas']
#imprimindo os dados de cada linha
for rows in frutas_pages.iter_rows(min_row=1, max_row=5):
    print(rows[0].value, rows[1].value, rows[2].value)