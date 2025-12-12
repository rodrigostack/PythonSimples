import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira GUI")
janela.geometry("300x200")

label = tk.Label(janela, text="Olá, mundo!")
label.pack()

janela.mainloop()
