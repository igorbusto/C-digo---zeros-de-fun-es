import PySimpleGUI as sg

class Newton:
    def __init__(self):
        sg.change_look_and_feel('LightBrown4')
        layout = [
            [sg.Text('                                         Método de Newton', size = (50,0))],
            [sg.Text(' ')],
            [sg.Text('Variavel X', size = (7,0)), sg.Input(size = (15,0)), sg.Text('Variavel N', size = (7,0)), sg.Input(size = (15,0))],
            
            [sg.Output(size = (60,20))],
            [sg.Button('OK')]
        ]
        

        self.janela = sg.Window("Dados para o calculo").layout(layout)

        
    #def segunda(self):
    #    sg.change_look_and_feel('LightBrown4')
    #    layout = [
    #        [sg.Text('                                         Teste2', size = (50,0))],
    #        [sg.Text(' ')],
    #        [sg.Text('asdasdasd', size = (7,0)), sg.Input(size = (15,0)), sg.Text('Vaasdffgel N', size = (7,0)), sg.Input(size = (15,0))],
    #        
    #        [sg.Output(size = (60,20))],
    #        [sg.Button('OK')]
    #   ]
    #    self.segundaJanela = sg.Window("Segunda tela").layout(layout)
        
    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            x = self.values[0]
            n = self.values[1]

            print('Valor X: ', x, '    Valor N: ', n)

            
            if(x > 3):
                self.janela.close()
                print("asdasd")
                layout = [
                [sg.Text('                                         Teste2', size = (50,0))],
                [sg.Text(' ')],
                [sg.Text('asdasdasd', size = (7,0)), sg.Input(size = (15,0)), sg.Text('Vaasdffgel N', size = (7,0)), sg.Input(size = (15,0))],
                
                [sg.Output(size = (60,20))],
                [sg.Button('OK')]
                ]
                self.segundaJanela = sg.Window("Segunda tela").layout(layout)
                #self.button, self.values = self.segundaJanela.Read()
           

        

tela = Newton()
tela.Iniciar()