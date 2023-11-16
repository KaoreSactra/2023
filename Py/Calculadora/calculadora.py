from tkinter import *

janela = Tk()

def bt_clic(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)

def bt_clear():
    global operador
    operador = ""
    input_text.set("")

def bt_igual():
    global operador
    resultado = str(eval(operador))
    input_text.set(resultado)
    operador = ""

operador = ""
input_text = StringVar()

input_frame = Frame(janela)
input_frame.pack()

input_field = Entry(input_frame, font=('arial', 20, 'bold'), textvariable=input_text, width=25, bg="light blue", bd=5, justify=RIGHT)
input_field.grid(row=0, column=0)

bt_frame = Frame(janela)
bt_frame.pack()

bt_1 = Button(bt_frame, font=('arial', 20, 'bold'), text="1", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(1))
bt_1.grid(row=2, column=0)

bt_2 = Button(bt_frame, font=('arial', 20, 'bold'), text="2", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(2))
bt_2.grid(row=2, column=1)

bt_3 = Button(bt_frame, font=('arial', 20, 'bold'), text="3", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(3))
bt_3.grid(row=2, column=2)

bt_4 = Button(bt_frame, font=('arial', 20, 'bold'), text="4", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(4))
bt_4.grid(row=3, column=0)

bt_5 = Button(bt_frame, font=('arial', 20, 'bold'), text="5", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(5))
bt_5.grid(row=3, column=1)

bt_6 = Button(bt_frame, font=('arial', 20, 'bold'), text="6", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(6))
bt_6.grid(row=3, column=2)

bt_7 = Button(bt_frame, font=('arial', 20, 'bold'), text="7", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(7))
bt_7.grid(row=4, column=0)

bt_8 = Button(bt_frame, font=('arial', 20, 'bold'), text="8", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(8))
bt_8.grid(row=4, column=1)

bt_9 = Button(bt_frame, font=('arial', 20, 'bold'), text="9", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(9))
bt_9.grid(row=4, column=2)

bt_0 = Button(bt_frame, font=('arial', 20, 'bold'), text="0", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic(0))
bt_0.grid(row=5, column=0)

bt_mais = Button(bt_frame, font=('arial', 20, 'bold'), text="+", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic("+"))
bt_mais.grid(row=2, column=3)

bt_menos = Button(bt_frame, font=('arial', 20, 'bold'), text="-", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic("-"))
bt_menos.grid(row=3, column=3)

bt_multiplicar = Button(bt_frame, font=('arial', 20, 'bold'), text="*", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic("*"))
bt_multiplicar.grid(row=4, column=3)

bt_dividir = Button(bt_frame, font=('arial', 20, 'bold'), text="/", width=6, height=2, bd=4, bg="light blue", command=lambda: bt_clic("/"))
bt_dividir.grid(row=5, column=3)

bt_clear = Button(bt_frame, font=('arial', 20, 'bold'), text="C", width=6, height=2, bd=4, bg="light blue", command=bt_clear)
bt_clear.grid(row=5, column=2)

bt_igual = Button(bt_frame, font=('arial', 20, 'bold'), text="=", width=6, height=2, bd=4, bg="light blue", command=bt_igual)
bt_igual.grid(row=5, column=1)

janela.mainloop()