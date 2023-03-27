#importando bibliotecas
from cProfile import label
from tkinter import *
from tkinter.ttk import *
from time import strftime

#título
root = Tk()
root.title('Relógio')

#funções para cálculo do horário
def relogio():
    horario = strftime('%H:%M:%S') #formatação do horário
    label.config(text=horario) #conversão do texto para horário
    label.after(1000,relogio) #função para atualizar horário a cada 1seg

#Formatação para fonte e cor
label = Label(root,font=('Helvetica',80), background='#000',foreground='#00FF04')
label.pack(anchor='center')

relogio()
mainloop()