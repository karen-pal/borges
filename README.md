# Borges Corpus
(WIP)

by Karen Palacio

<img src="https://i.imgur.com/iDJpsjf.png"/>

# Introducción
No hay muchos recursos sobre PLN sobre textos en español.

Este es un intento de contribuir al ecosistema del mismo.

En este repo hay dos datasets: uno se correponde con los textos completos de cuentos de Borges, más los análisis de sentimientos oración por oración, sin estructurar. Para el armado se scrapeó la página [Ciudad Seva](https://ciudadseva.com/autor/jorge-luis-borges/cuentos/) con Selenium. Para el análisis de sentimientos se usó [sentiment-analysis-spanish](https://pypi.org/project/sentiment-analysis-spanish/)

En este repositorio además vas a encontrar el script que generó este dataset.

# Contents

Available datasets so far in the datasets directory:

```
datasets/
├── borges_full_texts.pkl
└── sents.pkl
```

In this repo you'll find:

* `borges_full_texts.pkl`: in here you will find the complete scrapped texts in raw form, plus their metadata.
* `sents.pkl`: a list of dataframes, corresponding to each of the texts, in the same order. This is done with the library sentiment-analysis-spanish (More libraries comming soon)
* `scraper.py`: the script that builds the dataset with sentiment analysis sents.pkl
* `scrap_full_text.py`: the script that builds borges_full_texts.pkl
* `links.txt`: the links used by the script to search for the texts in the building of the dataset.

# TO DO

Complementar con más datasets de [otrxs autorxs](https://ciudadseva.com/biblioteca/indice-autor-cuentos/) y [otras bibliotecas digitales](https://ciudadseva.com/secciones/bibliotecas-digitales-publicas/)
