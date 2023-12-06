# Borges Corpus
(WIP)

by Karen Palacio

<img src="https://i.imgur.com/iDJpsjf.png"/>

# Últimas actualizaciones

- Actualicé el dataset de github para que tenga lo mismo pero en csv, manteniendo el formato. https://github.com/karen-pal/borges/tree/master/datasets/datasets_csv

- Además puse una notebook de muchos intentos de clustering con distintos algoritmos - ese trabajo lo tengo que seguir porque haciendo eso me di cuenta que no tiene mucho sentido cruzar todos los documentos con todos. Creo que es más interesante hacer topic modeling/clustering por autorx y realizar un dataset a partir de eso.
https://github.com/karen-pal/borges/blob/master/sentence_similarity.ipynb

# Introducción
No hay muchos recursos sobre PLN sobre textos en español.

Este es un intento de contribuir al ecosistema del mismo.

En este repo hay dos tipos de datasets: uno se correponde con los textos completos de cuentos de **autorxs latinoamericanxs**, y el otro contiene el análisis de sentimientos oración por oración de los textos. Para el armado se scrapeó la página [Ciudad Seva](https://ciudadseva.com/autor/jorge-luis-borges/cuentos/) con Selenium. Para el análisis de sentimientos se usó [sentiment-analysis-spanish](https://pypi.org/project/sentiment-analysis-spanish/)

En este repositorio además vas a encontrar los scripts que generan este dataset.

# Contents

Available datasets so far in the datasets directory:

```
datasets/
├── arlt_full_texts.pkl
├── arredondo_full_texts.pkl
├── benedetti_full_texts.pkl
├── bombal_full_texts.pkl
├── borges_full_texts.pkl
├── carrington_full_texts.pkl
├── davila_full_texts.pkl
├── de_la_parra_full_texts.pkl
├── garro_full_texts.pkl
├── links/
├── lispector_full_texts.pkl
├── lyra_full_texts.pkl
├── ocampo_full_texts.pkl
└── sents_borges.pkl
```

In this repo you'll find:

* `datasets/<author>_full_texts.pkl`: in here you will find the complete scraped texts in raw form, plus their metadata.
* `datasets/links/links_<author>.txt`: urls, sources of the text data. used for the scraping part of the dataset building.
* `sents_<author>.pkl`: a list of dataframes, corresponding to each of the texts, in the same order. This is done with the library sentiment-analysis-spanish (More libraries comming soon)
* `scraper.py`: the script that builds the dataset with sentiment analysis sents.pkl
* `full_text_scraper.py`: the script that builds `<author>_full_texts.pkl` given an author's name and the file with the links to scrap from.
* `links_scraper.py`: script that builds a `./datasets/links/links_<author>.txt` file, used in the scraping process.

# TO DO

## Expand vertically
Complementar con más datasets de [otrxs autorxs](https://ciudadseva.com/biblioteca/indice-autor-cuentos/) y [otras bibliotecas digitales](https://ciudadseva.com/secciones/bibliotecas-digitales-publicas/)

In doing so, do it with the following methodology:

* for each male author, look for a woman author.

> Trying to keep it balanced. Complicado teniendo en cuenta que incluso si hay un par de textos por autora, no se compara con la cantidad de textos de los hombres. Como no encuentro cantidad por autora voy a tener que hacer un esfuerzo a lo ancho ... es decir tener de cantidad de nombres.

## Expaind horizontally

Would be of interest to also collect:

Years of each story, genre(s), [author's nationality](https://ciudadseva.com/biblioteca/indice-paises-cuentos/)

> find a way to automate this. even just a CLI would do.


## Separate and expand genres

Hasta ahora solo estoy scrapeando cuentos. Estaría bueno tener [poemas](https://ciudadseva.com/biblioteca/indice-autor-poemas/), ["otros"](http://ciudadseva.com/biblioteca/indice-autor-otrostextos/) , [minicuentos](https://ciudadseva.com/biblioteca/indice-autor-minicuentos/).

## Incorporate authors:

### [blogspot también dividido por nacionalidad](http://cuentosdelatinoamerica.blogspot.com/search/label/Cuentistas%20de%20latinoam%C3%A9rica)

> Mujeres
```
    Isabel Allende (1942)
    Marcela Serrano (1951) ...
    Gioconda Belli. ...
    Sor Juana Inés de la Cruz (1651 - 1695) ...
    Alfonsina Storni (1892 - 1938) ...
    Gabriela Mistral (1889 - 1957) ...
    Juana de Ibarbourou (1892 - 1979) ...
```

### María Elena Walsh - Argentina:
* [Cuentos _ 5/6 cuentos](http://lasalademerlin.blogspot.com/2016/11/cinco-cuentos-cortos-de-maria-elena.html)
* [12 poemas](https://www.conmishijos.com/actividades-para-ninos/cuentos/12-bellos-y-divertidos-poemas-de-maria-elena-walsh-para-ninos/)
* [El ovillo - cuento](http://bpcd-mariaelenawalsh.blogspot.com/2013/06/cuento-el-ovillo-de-maria-elena-walsh.html)

### Gabriela Mistral - Chile:
* [1 cuento - el cántaro de greda](http://cuentosdelatinoamerica.blogspot.com/2011/06/el-cantaro-de-greda-gabriela-mistral.html)

### Claudia Cortalezzi - Argentina:
* [un cuento con camellos](http://cuentosdelatinoamerica.blogspot.com/2017/01/un-cuento-con-camellos-claudia.html)


### Alejandra D'Atri - Argentina:
* [Tan hombre](http://cuentosdelatinoamerica.blogspot.com/2015/11/tan-hombre-alejandra-datri.html)


> Hombres
### Salzano - Argentina:
* https://diceelwalter.blogspot.com/search/label/Daniel%20Salzano
* https://www.lavoz.com.ar/ciudadanos/salzano-algunos-de-sus-textos
### Rubén Darío - Nicaragua
### Horacio Quiroga
### Cortazar
### Macedonio Fernández
