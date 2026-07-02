import os
import re
import random
import subprocess
from datetime import datetime, timedelta

SOURCE = "calculadora_npk.py"
DIAS = 30            
DIAS_ATIVOS = 12     

BLOCOS = [
    ("feat: estrutura inicial e imports", r"^import tkinter"),
    ("feat: cálculo de quantidade de fertilizante por NPK", r"^def calcular\(\):"),
    ("feat: avaliação de nutrientes por tipo de solo", r"^def avaliar_nutrientes\(\):"),
    ("feat: função para limpar campos", r"^def limpar_campos\(\):"),
    ("feat: janela principal e layout base", r"^root = tk\.Tk\(\)"),
    ("feat: seletor de tipo de solo", r"^frame_tipo_solo = "),
    ("feat: seletor de adubação orgânica", r"^frame_adubacao_organica = "),
    ("feat: campos de recomendação de NPK", r"^frame_npk = "),
    ("feat: campos de composição do fertilizante", r"^frame_fertilizante = "),
    ("feat: painel de avaliação dos nutrientes", r"^frame_avaliacao = "),
    ("feat: botões de calcular, avaliar e limpar", r"^btn_frame = "),
    ("feat: exibição do resultado total", r"^resultado_label = tk\.Label\(left_frame"),
    ("feat: painel de cálculo individual de N, P e K", r"^frame_calculo_individual = "),
    ("feat: painel com as fórmulas utilizadas", r"^frame_formulas = "),
    ("feat: inicia o loop principal da interface", r"^root\.mainloop\(\)"),
]

GITIGNORE = "__pycache__/\n*.pyc\n.venv/\n.idea/\n.vscode/\n"

README_1 = """# Calculadora NPK

Calculadora de adubação para o agro, feita em Python com Tkinter.
"""

README_2 = """# Calculadora NPK

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
"""

def sh(*args, env=None):
    subprocess.run(args, check=True, env=env, stdout=subprocess.DEVNULL)

def commit(msg, data):
    iso = data.strftime("%Y-%m-%dT%H:%M:%S")
    env = {**os.environ, "GIT_AUTHOR_DATE": iso, "GIT_COMMITTER_DATE": iso}
    sh("git", "add", "-A")
    sh("git", "commit", "-m", msg, "--quiet", env=env)

def escrever(nome, conteudo):
    with open(nome, "w", encoding="utf-8") as f:
        f.write(conteudo)

def main():
    with open(SOURCE, encoding="utf-8") as f:
        codigo = f.read()

    posicoes = [re.search(p, codigo, re.M).start() for _, p in BLOCOS]

    passos = [
        ("chore: adiciona .gitignore", lambda: escrever(".gitignore", GITIGNORE)),
        ("docs: adiciona README inicial", lambda: escrever("README.md", README_1)),
    ]
    for i, (msg, _) in enumerate(BLOCOS):
        fim = posicoes[i + 1] if i + 1 < len(BLOCOS) else len(codigo)
        trecho = codigo[:fim]
        passos.append((msg, lambda t=trecho: escrever(SOURCE, t)))
    passos.append(("docs: documenta funcionalidades, fórmulas e execução",
                   lambda: escrever("README.md", README_2)))

    INICIO = datetime(2026, 7, 1)
    dias = random.sample(range(31), DIAS_ATIVOS)   
    pesos = [random.choice([1, 1, 2, 3, 5]) for _ in dias]

    datas = []
    for _ in passos:
        d = random.choices(dias, weights=pesos)[0]
        datas.append(INICIO + timedelta(days=d,
                                        hours=random.randint(8, 21),
                                        minutes=random.randint(0, 59)))
    datas.sort()  

    if not os.path.isdir(".git"):
        sh("git", "init", "-b", "main")

    for (msg, acao), data in zip(passos, datas):
        acao()
        commit(msg, data)

    print(f"{len(passos)} commits criados.")

if __name__ == "__main__":
    main()