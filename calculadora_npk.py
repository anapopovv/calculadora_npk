import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    try:
        n_recomendado = float(entry_n.get() or 0)
        p_recomendado = float(entry_p.get() or 0)
        k_recomendado = float(entry_k.get() or 0)

        n_fert = float(entry_n_fert.get() or 0) / 100
        p_fert = float(entry_p_fert.get() or 0) / 100
        k_fert = float(entry_k_fert.get() or 0) / 100

        if n_fert == 0 or p_fert == 0 or k_fert == 0:
            messagebox.showerror("Erro", "A composição do fertilizante não pode ter 0% em nenhum nutriente!")
            return

        qtd_n = n_recomendado / n_fert
        qtd_p = (p_recomendado / 0.437) / p_fert
        qtd_k = (k_recomendado / 0.830) / k_fert

        if any(qtd < 0 for qtd in [qtd_n, qtd_p, qtd_k]):
            messagebox.showerror("Erro", "Valores negativos não são permitidos!")
            return

        qtd_fertilizante = max(qtd_n, qtd_p, qtd_k)
        
        resultado_label.config(text=f"Quantidade total: {qtd_fertilizante:.2f} kg/ha")
        resultado_individual_n.config(text=f"{qtd_n:.2f} kg/ha")
        resultado_individual_p.config(text=f"{qtd_p:.2f} kg/ha")
        resultado_individual_k.config(text=f"{qtd_k:.2f} kg/ha")

        valor_n = float(entry_n_fert.get())
        if valor_n < 4:
            resultado_nitrogenio.config(text="Baixo", fg="red")
        elif 4 <= valor_n <= 9:
            resultado_nitrogenio.config(text="Médio", fg="orange")
        else:
            resultado_nitrogenio.config(text="Alto", fg="green")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos!")

