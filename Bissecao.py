from math import *
import numpy as np
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('f(x)'), sg.Input(size=(15,0))],
            [sg.Text('a(+)'), sg.Input(size=(3,0))],
            [sg.Text('b(-)'), sg.Input(size=(3,0))],
            [sg.Button('Executar'), sg.Button('Limpar')],
            [sg.Text('Resultado')],
            [sg.Output(size=(40,15))]
        ]
        # Janela
        self.janela = sg.Window("Somatório PF").layout(layout)
    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values= self.janela.Read()
            def func(expr, x):
                return eval(expr)

            input_expr = self.values[0]
            a = eval(self.values[1])
            b = eval(self.values[2])

            def bisection(a,b): 
                if (func(input_expr, a) * func(input_expr, b) >= 0): 
                    print("Você não inseriu valores válidos para a ou b\n") 
                    return
                c = a 
                iteracoes = 0
                while ((b-a) >= 0.01): 
                    iteracoes += 1
                    # Ponto médio
                    c = (a+b)/2
                    # Checar se ponto médio é a raiz
                    if (func(input_expr,c) == 0.0): 
                        break
                    # Deicidir o lado da repeitção (+/-)
                    if (func(input_expr,c)*func(input_expr,a) < 0): 
                        b = c 
                    else: 
                        a = c 
                print("Raiz:","%.4f"%c) 
                print("Iterações:", iteracoes)
            bisection(a, b)
tela = TelaPython()
tela.Iniciar()