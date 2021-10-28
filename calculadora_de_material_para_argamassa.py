import PySimpleGUI as sg

class calculo_argamassa:
    def __init__(self):
        sg.theme ('Material1')
        layout = [
            [sg.Text('Informe a area em m²: ',size=(17,0)),sg.Input(size=(15,0),key ='area')],
            [sg.Text('Informe a altura em metros: ',size=(17,0)),sg.Input(size=(15,0),key ='altura')],
            [sg.Text('Informe o traço desejado: ')],
            [sg.Radio('1/3','traco', key = 'traco'),sg.Radio('1/4', 'traco')],
            [sg.Button('Calcular')],
            [sg.Output(size= (50,10))],
        ]
        self.janela = sg.Window ('Calculo de material para Argamassa').layout(layout)


    def Iniciar(self):
        while True:
            #mantem Janela aberta
            self.button, self.values = self.janela.Read ()

            area = self.values['area']
            area = float(area)
            altura = self.values['altura']
            altura = float(altura)
            traco = self.values['traco']
            volume = area * altura

            if traco == True:
                traco = 4
            else:
                traco = 5

            traco = int(traco)

            prop = volume / traco
            cimento = (1200 * prop) * 1.1
            cimento_saco = cimento / 50
            if traco == 4:
                traco_areia = 3
            elif traco == 5:
                traco_areia = 4
            areia = (prop * traco_areia) * 1.1
            areia_saco = (areia * 60)
            areia_saco = int(areia_saco)
            cimento_saco = int(cimento_saco)
            print (f'Cimento: {cimento:.2f} kg ou {cimento_saco:.2f} sacos de cimento (50kg)')
            print (f'Areia: {areia:.2f} m³ ou {areia_saco:.0f} sacos de areia (20kg)')
            print('________________________________________________')

tela = calculo_argamassa()
tela.Iniciar()

