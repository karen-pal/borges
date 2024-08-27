# Borges Corpus
(WIP permanente)

by Karen Palacio

<a href="https://docs.google.com/presentation/d/1ROmh6rz_8Oblh-yGTz8aypbHnaxXx2R5usZnBOdz3lk/edit?usp=sharing">Slides introductorias sobre la metodología de armado y la estructura del dataset<a/>

<img src="https://i.imgur.com/iDJpsjf.png"/>

# Uso y licencia
Yo, Karen Palacio aka kardaver, autorizo el uso de este dataset para cualquier tipo de uso, mientras se me de reconocimiento de autoría (y en lo posible se me informe - para dejar asentado aquí para qué ha sido utilizado y que sirva a otras personas a aprender sobre NLP)


# Últimas actualizaciones

- Agregué una versión humana del dataset con sentiment analysis de la obra de borges, ahora bien anotado y con formato csv - para ser amable con el resto de los mortales. https://github.com/karen-pal/borges/blob/master/datasets/borges_sentiment_corpus.csv

- Agregué una versión compacta del dataset, conteniendo todos los cuentos de todes les autores en un solo archivo csv - para su uso con librerías de huggingface: https://github.com/karen-pal/borges/blob/master/datasets/full_corpus.csv

- Actualicé el dataset de github para que tenga lo mismo pero en csv, manteniendo el formato. https://github.com/karen-pal/borges/tree/master/datasets/datasets_csv

- Además puse una notebook de muchos intentos de clustering con distintos algoritmos - ese trabajo lo tengo que seguir porque haciendo eso me di cuenta que no tiene mucho sentido cruzar todos los documentos con todos. Creo que es más interesante hacer topic modeling/clustering por autorx y realizar un dataset a partir de eso.
https://github.com/karen-pal/borges/blob/master/sentence_similarity.ipynb

# Introducción
No hay muchos recursos sobre PLN sobre textos en español.

Este es un intento de contribuir al ecosistema del mismo.

En este repo hay dos tipos de datasets: uno se correponde con los textos completos de cuentos de **autorxs latinoamericanxs**, y el otro contiene el análisis de sentimientos oración por oración de los textos de borges. Para el armado se scrapeó la página [Ciudad Seva](https://ciudadseva.com/autor/jorge-luis-borges/cuentos/) con Selenium. Para el análisis de sentimientos se usó [sentiment-analysis-spanish](https://pypi.org/project/sentiment-analysis-spanish/)

En este repositorio además vas a encontrar los scripts que generan este dataset.

Si los querés correr vos, tenés que saber que hay una dependencia fuerte con pandas<2.0.0, y vas a necesitar keras, tensorflow, numpy, pickle,

# Contents

Available datasets so far in the datasets directory:

```

datasets/
├── borges_sentiment_corpus.csv
├── full_corpus.csv
├── datasets_csv
│   ├── alonso_m_full_texts.csv
│   ├── anderson_imbert_full_texts.csv
│   ├── arenal_full_texts.csv
│   ├── arguedas_full_texts.csv
│   ├── arlt_full_texts.csv
│   ├── arredondo_full_texts.csv
│   ├── arreola_full_texts.csv
│   ├── baldomero_full_texts.csv
│   ├── bareiro_saguier_full_texts.csv
│   ├── benedetti_full_texts.csv
│   ├── bioy_casares_full_texts.csv
│   ├── bombal_full_texts.csv
│   ├── borges_full_texts.csv
│   ├── bosch_full_texts.csv
│   ├── carpentier_full_texts.csv
│   ├── carrington_full_texts.csv
│   ├── cortazar_full_texts.csv
│   ├── dabove_full_texts.csv
│   ├── davila_full_texts.csv
│   ├── de_la_parra_full_texts.csv
│   ├── donoso_full_texts.csv
│   ├── echeverría_full_texts.csv
│   ├── edwards_j_full_texts.csv
│   ├── fernandez_m_full_texts.csv
│   ├── freyre_full_texts.csv
│   ├── gallegos_full_texts.csv
│   ├── garmendia_full_texts.csv
│   ├── garro_full_texts.csv
│   ├── grullon_full_texts.csv
│   ├── gudino_kieffer_full_texts.csv
│   ├── guiraldes_full_texts.csv
│   ├── hernandez_f_full_texts.csv
│   ├── huidobro_full_texts.csv
│   ├── lezama_lima_full_texts.csv
│   ├── lillo_full_texts.csv
│   ├── lispector_full_texts.csv
│   ├── lopez_y_fuentes_full_texts.csv
│   ├── lyra_full_texts.csv
│   ├── monterroso_full_texts.csv
│   ├── mutis_full_texts.csv
│   ├── ocampo_full_texts.csv
│   ├── palacio_full_texts.csv
│   ├── paz_o_full_texts.csv
│   ├── pinera_full_texts.csv
│   ├── pitol_full_texts.csv
│   ├── reyes_full_texts.csv
│   ├── ribeyro_full_texts.csv
│   ├── rivera_a_full_texts.csv
│   ├── romero_de_terreros_full_texts.csv
│   ├── ruben_dario_full_texts.csv
│   ├── rulfo_full_texts.csv
│   ├── salarrue_full_texts.csv
│   ├── torri_full_texts.csv
│   ├── valades_full_texts.csv
│   ├── vidales_full_texts.csv
│   ├── walsh_r_full_texts.csv
│   ├── wilcock_full_texts.csv
│   └── zeledon_full_texts.csv
```

In this repo you'll find:

* `datasets/datasets_pkl/<author>_full_texts.pkl`: in here you will find the complete scraped texts in raw form, plus their metadata.
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
