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

In this repo you'll find:

* `scraper.py`: a script to build the dataset.
* `links.txt`: the links used by the script to search for the texts in the building of the dataset.
* `sents.pckl`: a list of dataframes, corresponding to each of the Dataset's texts.
* `borges_base.csv`: the full dataset, with the full texts.
