import tkinter as tk
from tkinter import messagebox

def somar():
    try:
        valor1 = float(entry_valor1.get())
        valor2 = float(entry_valor2.get())
        resultado = valor1 + valor2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")
janela.geometry("300x200")

# Campo Valor 1
label1 = tk.Label(janela, text="Valor 1:")
label1.pack()
entry_valor1 = tk.Entry(janela)
entry_valor1.pack()

# Campo Valor 2
label2 = tk.Label(janela, text="Valor 2:")
label2.pack()
entry_valor2 = tk.Entry(janela)
entry_valor2.pack()

# Botão para calcular
btn_calcular = tk.Button(janela, text="Calcular", command=somar)
btn_calcular.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack()

# Iniciar interface
janela.mainloop()
