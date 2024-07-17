import tkinter as tk

class Tela:
    def clicou(self):
        self.lbl_clicou =   tk.Label(self.janela, text='Clicou')
        self.lbl_clicou.pack()
    def __init__(self, master):
        self.janela = master
        self.lbl_usuario = tk.Label(self.janela, text='Nome de usuário:',
                                 bg='aquamarine',
                                 fg='blue',
                                 font=('Ubuntu', 24,'bold'),
                                 width=100,
                                 pady=50,
                                 padx= 20,
                                 height=3,



                                 )
        self.lbl_usuario.pack()
        ent_usuario = tk.Entry(self.janela)
        ent_usuario.pack()


        tk.Label(self.janela, text="Senha:")
        self.ent_senha = tk.Entry(self.janela)
        self.ent_senha.pack()

        self.btn_acessar = tk.Button(self.janela, text='ACESSA AÍ', command= self.clicou)
        self.btn_acessar.pack()




janela = tk.Tk()
app = Tela(janela)
janela.mainloop()


