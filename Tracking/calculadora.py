from tkinter import *

# Variáveis
num1 = 1
num2 = 1
num3 = 0
symbol = ""

# Funções
def sum():
    symbol = "+"
    num3 = num1 + num2

def subtraction():
    symbol = "-"
    num3 = num1 - num2

def division():
    symbol = "/"
    num3 = num1 / num2

def multiplication():
    symbol = "x"
    num3 = num1 * num2

def clear():
    symbol = ""
    num3 = 0

# Janela
janela = Tk() # Definindo janela

# Titulo
janela.title('Calculator')
janela.geometry('200x100')
janela.resizable(False, False)

# dentro da janela
a1 = Label(janela, text=num1)
a1.grid(column=0, row=0, padx=10, pady=10)

a2 = Label(janela, text=symbol)
a2.grid(column=1, row=0, padx=10, pady=10)

a3 = Label(janela, text=num2)
a3.grid(column=2, row=0, padx=10, pady=10)

a4 = Label(janela, text="=")
a4.grid(column=3, row=0, padx=10, pady=10)

a5 = Label(janela, text=num3)
a5.grid(column=4, row=0, padx=10, pady=10)

b1 = Button(janela, text="+", command=sum)
b1.grid(column=0, row=1, padx=10, pady=10)

b2 = Button(janela, text="-", command=subtraction)
b2.grid(column=1, row=1, padx=10, pady=10)

b3 = Button(janela, text="/", command=division)
b3.grid(column=2, row=1, padx=10, pady=10)

b4 = Button(janela, text="x", command=multiplication)
b4.grid(column=3, row=1, padx=10, pady=10)

b5 = Button(janela, text="", command=clear)
b5.grid(column=4, row=1, padx=10, pady=10)

# fazer a janela continuar sendo exibida
janela.mainloop()