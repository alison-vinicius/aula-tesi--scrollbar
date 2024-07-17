import tkinter as tk


class Tela:
    def clicou_check(self):
        if self.var_argentina.get() == 0 or self.var_brasil.get() == 0:
            self.lbl_mostrar['text'] = ''
        if self.var_brasil.get() == 1:
            self.lbl_mostrar['text'] = 'Nunca sera'
        if self.var_argentina.get() == 1:
            self.lbl_mostrar.config(text="campeão")
        if self.var_argentina.get() and self.var_brasil.get() == 1:
            self.lbl_mostrar['text'] = ''

    def clicou_radio(self):
        self.lbl_mostrar_radio['text'] = self.carioca.get()

    def __init__(self, master):
        self.janela = master

        # EXEMPLO CEHCK ----------------------------------------------------------------------------------
        # self.var_brasil = tk.IntVar()
        # self.var_argentina = tk.IntVar()

        # self.cbt_brasil = tk.Checkbutton(self.janela,
        #                                  text='Brasil',
        #                                  variable=self.var_brasil,
        #                                  command=self.clicou_check)
        # self.cbt_brasil.pack()
        # self.cbt_argetina = tk.Checkbutton(self.janela,
        #                                  text='Argentina',
        #                                  variable=self.var_argentina,
        #                                  command=self.clicou_check)
        # self.cbt_argetina.pack()

        # self.lbl_mostrar = tk.Label(self.janela)
        # self.lbl_mostrar.pack()

        # EXEMPLO BUTTON RADIO ----------------------------------------------------------------------

        # self.rbt1 = tk.RADIOBUTTON(self.janela, text='1', value=valor[0], setcolor='red')
        # self.rbt2 = tk.RADIOBUTTON(self.janela, text='2', value=valor[1], setcolor='blue')

        valor = [1, 2]
        dicionario = {
            1: 'flamengo',
            2: 'vasco',
            3: 'bota fogo'
        }

        self.carioca = tk.StringVar()

        for (v, t) in dicionario.items():
            self.rbt = tk.Radiobutton(self.janela, text=t, value=v, variable=self.carioca,
                                      command=self.clicou_radio).pack()

        self.lbl_mostrar_radio = tk.Label(self.janela)
        self.lbl_mostrar_radio.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()