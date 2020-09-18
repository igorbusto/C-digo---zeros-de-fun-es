import PySimpleGUI as sg

class TelaMenu:
    sg.theme('Light Blue 3')

    def button1(self=None):
        from Metodos.Bissecao import TelaBissecao

    def button2(self=None):
        from Metodos.Newton import Newton

    dispatch_dictionary = {'Bisseção':button1, 'Newton':button2}
    layout = [[sg.Text('Selecione um método', auto_size_text=True)],
            [sg.Button('Bisseção'), sg.Button('Newton'), sg.Quit('Encerrar')]]

    window = sg.Window('Métodos', layout)
    while True:
        event, value = window.read()
        if event in ('Encerrar', sg.WIN_CLOSED):
            break
        if event in dispatch_dictionary:
            func_to_call = dispatch_dictionary[event]
            func_to_call()
        else:
            print('Event {} não encontrado'.format(event))

    window.close()
    sg.popup_ok('Menu finalizado!')
menu = TelaMenu()