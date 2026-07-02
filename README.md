# Calculadora NPK

Calculadora de adubação para o agro, feita em Python com Tkinter.

## Funcionalidades
- Calcula a quantidade de fertilizante (kg/ha) a partir da recomendação de N, P e K
- Considera a composição (%) do fertilizante escolhido
- Classifica fósforo, potássio e nitrogênio do solo (baixo, médio, alto) por tipo de solo
- Resultado individual por nutriente

## Fórmulas
- Nitrogênio: `Qtd = N_recomendado / %N_fertilizante`
- Fósforo: `Qtd = (P_recomendado / 0.437) / %P_fertilizante`
- Potássio: `Qtd = (K_recomendado / 0.830) / %K_fertilizante`

## Como rodar
```bash
python calculadora_npk.py
```
