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

def avaliar_nutrientes():
    try:
        fosforo = float(entry_fosforo.get() or 0)
        potassio = float(entry_potassio.get() or 0)
        nitrogenio = float(entry_nitrogenio.get() or 0)
        tipo_solo = combo_tipo_solo.get()

        if tipo_solo == "Solo Argiloso":
            if nitrogenio < 6:
                classificacao_n = "Baixo"
            elif 6 <= nitrogenio <= 12:
                classificacao_n = "Médio"
            else:
                classificacao_n = "Alto"
        elif tipo_solo == "Solo Arenoso":
            if nitrogenio < 3:
                classificacao_n = "Baixo"
            elif 3 <= nitrogenio <= 8:
                classificacao_n = "Médio"
            else:
                classificacao_n = "Alto"
        elif tipo_solo == "Solo Siltoso":
            if nitrogenio < 4:
                classificacao_n = "Baixo"
            elif 4 <= nitrogenio <= 9:
                classificacao_n = "Médio"
            else:
                classificacao_n = "Alto"
        else:
            classificacao_n = "Indefinido"

        if tipo_solo == "Solo Argiloso":
            if fosforo < 6:
                classificacao_p = "Baixo"
            elif 6 <= fosforo <= 10:
                classificacao_p = "Médio"
            else:
                classificacao_p = "Alto"
        elif tipo_solo == "Solo Arenoso":
            if fosforo < 4:
                classificacao_p = "Baixo"
            elif 4 <= fosforo <= 8:
                classificacao_p = "Médio"
            else:
                classificacao_p = "Alto"
        elif tipo_solo == "Solo Siltoso":
            if fosforo < 5:
                classificacao_p = "Baixo"
            elif 5 <= fosforo <= 9:
                classificacao_p = "Médio"
            else:
                classificacao_p = "Alto"
        else:
            classificacao_p = "Indefinido"

        if tipo_solo == "Solo Argiloso":
            if potassio < 15:
                classificacao_k = "Baixo"
            elif 15 <= potassio <= 25:
                classificacao_k = "Médio"
            else:
                classificacao_k = "Alto"
        elif tipo_solo == "Solo Arenoso":
            if potassio < 12:
                classificacao_k = "Baixo"
            elif 12 <= potassio <= 20:
                classificacao_k = "Médio"
            else:
                classificacao_k = "Alto"
        elif tipo_solo == "Solo Siltoso":
            if potassio < 10:
                classificacao_k = "Baixo"
            elif 10 <= potassio <= 18:
                classificacao_k = "Médio"
            else:
                classificacao_k = "Alto"
        else:
            classificacao_k = "Indefinido"

        analise_label.config(
            text=f"Fósforo: {classificacao_p}\nPotássio: {classificacao_k}\nNitrogênio: {classificacao_n}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")


def limpar_campos():

    entry_n.delete(0, 'end')
    entry_p.delete(0, 'end')
    entry_k.delete(0, 'end')
    entry_n_fert.delete(0, 'end')
    entry_p_fert.delete(0, 'end')
    entry_k_fert.delete(0, 'end')
    entry_fosforo.delete(0, 'end')
    entry_potassio.delete(0, 'end')
    entry_nitrogenio.delete(0, 'end')
    
    combo_tipo_solo.current(0)
    combo_adubacao_organica.current(0)
    
    resultado_label.config(text='')
    resultado_individual_n.config(text='0.00 kg/ha')
    resultado_individual_p.config(text='0.00 kg/ha')
    resultado_individual_k.config(text='0.00 kg/ha')
    resultado_nitrogenio.config(text='')
    analise_label.config(text='')

