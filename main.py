from tkinter import *


class Calculadora(Tk):
    def __init__(self):
        super().__init__()


        self.title('Calculadora')
        self.resizable(0, 0)
        self.geometry('+800+300')


        self.Comecar()


    def Comecar(self):

        self.Tela = Entry(self, width=40, font='Arial 18')
        self.Tela.grid(row=0, columnspan=4, sticky='NESW')

        self.Limpar = Button(self, text='C', command=self.Limpar_Tela, font='Arial 15')
        self.Limpar.grid(row=1, column=0, sticky='EW')

        self.Parentese_1 = Button(self, text='(', command=lambda N='(':self.Conta(N), font='Arial 15')
        self.Parentese_1.grid(row=1, column=1, sticky='EW')

        self.Parentese_2 = Button(self, text=')', command=lambda N=')':self.Conta(N), font='Arial 15')
        self.Parentese_2.grid(row=1, column=2, sticky='EW')


        Numeros = ['123', '456', '789']

        Valor_Row = 1


        for Numero in Numeros:
            Valor_Row += 1
            Valor_Column = 0

            for N in Numero:
                self.Botão = Button(self, text=N, font='Arial 15', command=lambda N=N:self.Conta(N))
                self.Botão.grid(row=Valor_Row, column=Valor_Column, sticky='EW')

                Valor_Column += 1


        Expressoes_Mat = ['+', '-', 'x', '/']

        Valor_Row = 0

        for Expressão in Expressoes_Mat:
            Valor_Row += 1

            self.Botão_Expr = Button(self, text=Expressão, font='Arial 15', command=lambda N=Expressão: self.Conta(f' {N} '))
            self.Botão_Expr.grid(row=Valor_Row, column=3, sticky='EW')


        Row_5 = ['%', '0', ',']

        Valor_Column = 0

        for Final_5 in Row_5:
            self.Botão_5 = Button(self, text=Final_5, font='Arial 15', command=lambda N=Final_5: self.Conta(N))
            self.Botão_5.grid(row=5, column=Valor_Column, sticky='EW')

            Valor_Column += 1


        self.Resultado = Button(self, text='=', font='Arial 15', command=self.Result, bg='#2e9922')
        self.Resultado.grid(row=5, column=3, sticky='EW')


    def Conta(self, Numero):
        self.Tela.insert(END, Numero)


    def Limpar_Tela(self):
        self.Tela.delete(0, 'end')


    def Result(self):
        Conta = str(self.Tela.get())

        Conta = Conta.replace('%', ' / 100')
        Conta = Conta.replace('x', '*')
        Conta = Conta.replace(',', '.')


        try:
            Resultado = eval(Conta)

            self.Tela.delete(0, 'end')

            Resultado = str(Resultado).replace('.', ',')


            self.Tela.insert(END, Resultado)

        except:
            self.Tela.delete(0, 'end')
            self.Tela.insert(END, 'ERROR')


if __name__ == '__main__':
    Calculadora().mainloop()
