import pandas as pd
import matplotlib.pyplot as plt

arquivo = "20260701.as-org2info.txt"

dados = []

lendo = False

with open(arquivo, encoding="utf-8") as f:
    for linha in f:

        if linha.startswith("# format:org_id"):
            lendo = True
            continue

        if linha.startswith("# format:aut"):
            break

        if not lendo:
            continue

        if linha.startswith("#") or linha.strip() == "":
            continue

        org_id, changed, org_name, country, source = linha.strip().split("|")

        dados.append({
            "org": org_name,
            "country": country
        })

df = pd.DataFrame(dados)

# GRÁFICO 1

top = df["country"].value_counts().head(10)

plt.figure(figsize=(8,5))
top.plot(kind="bar")
plt.title("Top 10 países por quantidade de organizações registradas")
plt.ylabel("Número de organizações")
plt.xlabel("País")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico1_top_paises.png", dpi=300)

# GRÁFICO 2

us_cn = df[df.country.isin(["US","CN"])]

contagem = us_cn.country.value_counts()

plt.figure(figsize=(5,5))
contagem.plot(kind="bar")
plt.title("Organizações registradas: EUA x China")
plt.ylabel("Quantidade")
plt.xlabel("")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico2_us_cn.png", dpi=300)

print(contagem)
