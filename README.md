# BGP Analysis

Análise da infraestrutura global da Internet utilizando dados públicos de Sistemas Autônomos (ASes), com foco na comparação entre Estados Unidos e China.

Este repositório contém os scripts utilizados para processamento dos dados e geração dos gráficos apresentados no artigo sobre a influência de grandes provedores globais e a relação entre a infraestrutura BGP e a rivalidade tecnológica entre EUA e China.

## Objetivo

O objetivo deste projeto é analisar a distribuição geográfica de organizações associadas a Sistemas Autônomos (Autonomous Systems - ASes) e observar possíveis padrões de concentração da infraestrutura da Internet.

A análise utiliza dados públicos disponibilizados pelo **CAIDA (Center for Applied Internet Data Analysis)**, através da base **AS Rank**, que reúne informações sobre organizações responsáveis por Sistemas Autônomos.

## Dados utilizados

Os dados utilizados neste projeto foram obtidos a partir da base:

- **CAIDA AS Rank**
  - https://asrank.caida.org/

A base fornece informações sobre Sistemas Autônomos e organizações associadas, incluindo país de registro.

## Métricas analisadas

Foram utilizadas as seguintes métricas:

- Quantidade de organizações registradas por país;
- Comparação entre organizações associadas aos Estados Unidos e China;
- Distribuição geográfica dos operadores de Sistemas Autônomos.

## Requisitos

- Python 3+
- pandas
- matplotlib

Instale as dependências:

```bash
pip install pandas matplotlib
```

Rode o script:

```bash
pyhon main.py
```
## Licença

Este projeto está disponibilizado sob a licença MIT. Você pode utilizar, modificar e redistribuir o código, desde que mantenha os créditos aos autores.

