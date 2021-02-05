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
├── arlt_full_texts.pkl
├── arredondo_full_texts.pkl
├── benedetti_full_texts.pkl
├── borges_full_texts.pkl
├── links
│   ├── links_arlt.txt
│   ├── links_arredondo.txt
│   ├── links_benedetti.txt
│   ├── links_borges.txt
│   └── links_silvina_ocampo.txt
├── ocampo_full_texts.pkl
└── sents_borges.pkl
```

In this repo you'll find:

* `datasets/<author>_full_texts.pkl`: in here you will find the complete scraped texts in raw form, plus their metadata.
* `datasets/links/links_<author>.txt`: sources of the text data. used for the scraping part of the dataset building.
* `sents_<author>.pkl`: a list of dataframes, corresponding to each of the texts, in the same order. This is done with the library sentiment-analysis-spanish (More libraries comming soon)
* `scraper.py`: the script that builds the dataset with sentiment analysis sents.pkl
* `scrap_full_text.py`: the script that builds borges_full_texts.pkl
* ``:

# TO DO

## Expand vertically
Complementar con más datasets de [otrxs autorxs](https://ciudadseva.com/biblioteca/indice-autor-cuentos/) y [otras bibliotecas digitales](https://ciudadseva.com/secciones/bibliotecas-digitales-publicas/)

In doing so, do it with the following methodology:

* for each male author, look for a woman author.

> Trying to keep it balanced.

## Expaind horizontally

Would be of interest to also collect:

Years of each story, genre(s), author's nationality

> find a way to automate this. even just a CLI would do.
