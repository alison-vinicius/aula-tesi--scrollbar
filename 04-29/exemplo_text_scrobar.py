import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        hino = """
        visca barça 
        y visca catalunya
        """
        self.src_musica = tk.Scrollbar(self.janela)
        self.txt_musica = tk.Text(self.janela, height=4, width=40, yscrollcommand=self.src_musica.set)

        self.txt_musica.pack(side=tk.LEFT, fill=tk.BOTH)
        self.txt_musica.insert(tk.END, hino)

        self.src_musica.config(command=self.txt_musica.yview())
        self.src_musica.pack(side=tk.RIGHT, fill = tk.Y)


        self.txt_scrolledtext = ScrolledText(self.janela)
        self.txt_scrolledtext.pack()


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()