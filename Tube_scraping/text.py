with open('op.txt', 'r') as arquivo:
        texto = arquivo.read()

# Calcule o comprimento total do texto
comprimento_total = len(texto)

# Calcule o tamanho de cada parte (divisão inteira)
tamanho_parte = comprimento_total // 20

# Divida o texto em 4 partes iguais

parte1 = texto[0*tamanho_parte:1*tamanho_parte]
parte2 = texto[1*tamanho_parte:2*tamanho_parte]
parte3 = texto[2*tamanho_parte:3*tamanho_parte]
parte4 = texto[3*tamanho_parte:4*tamanho_parte]
parte5 = texto[4*tamanho_parte:5*tamanho_parte]
parte6 = texto[5*tamanho_parte:6*tamanho_parte]
parte7 = texto[6*tamanho_parte:7*tamanho_parte]
parte8 = texto[7*tamanho_parte:8*tamanho_parte]
parte9 = texto[8*tamanho_parte:9*tamanho_parte]
parte10 = texto[9*tamanho_parte:10*tamanho_parte]
parte11 = texto[10*tamanho_parte:11*tamanho_parte]
parte12 = texto[11*tamanho_parte:12*tamanho_parte]
parte13 = texto[12*tamanho_parte:13*tamanho_parte]
parte14 = texto[13*tamanho_parte:14*tamanho_parte]
parte15 = texto[14*tamanho_parte:15*tamanho_parte]
parte16 = texto[15*tamanho_parte:16*tamanho_parte]
parte17 = texto[16*tamanho_parte:17*tamanho_parte]
parte18 = texto[17*tamanho_parte:18*tamanho_parte]
parte19 = texto[18*tamanho_parte:19*tamanho_parte]
parte20 = texto[19*tamanho_parte:20*tamanho_parte]

with open("op1.txt", "w") as opf:
        opf.write(parte1)
with open("op2.txt", "w") as opf:
        opf.write(parte2)
with open("op3.txt", "w") as opf:
        opf.write(parte3)
with open("op4.txt", "w") as opf:
        opf.write(parte4)
with open("op5.txt", "w") as opf:
        opf.write(parte5)
with open("op6.txt", "w") as opf:
        opf.write(parte6)
with open("op7.txt", "w") as opf:
        opf.write(parte7)
with open("op8.txt", "w") as opf:
        opf.write(parte8)
with open("op9.txt", "w") as opf:
        opf.write(parte9)
with open("op10.txt", "w") as opf:
        opf.write(parte10)
with open("op11.txt", "w") as opf:
        opf.write(parte11)
with open("op12.txt", "w") as opf:
        opf.write(parte12)
with open("op13.txt", "w") as opf:
        opf.write(parte13)
with open("op14.txt", "w") as opf:
        opf.write(parte14)
with open("op15.txt", "w") as opf:
        opf.write(parte15)
with open("op16.txt", "w") as opf:
        opf.write(parte16)
with open("op17.txt", "w") as opf:
        opf.write(parte17)
with open("op18.txt", "w") as opf:
        opf.write(parte18)
with open("op19.txt", "w") as opf:
        opf.write(parte19)
with open("op20.txt", "w") as opf:
        opf.write(parte20)

