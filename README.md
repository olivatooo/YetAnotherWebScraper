# (Y)et(A)nother(W)eb(S)craper

Um webscraper de notícias utilizando o princípio **aberto-fechado** e **responsabilidade única**.

Antes de rodar, instale as dependencias:
`pip install -r requirements`

Exemplos de uso:
Para fazer o download como json:
`./yaws.py g1 noticias_de_hoje`

Para fazer o download como csv:
`./yaws.py g1 noticias_de_hoje --writer csv`

Este projeto utiliza duas Design Patterns para suportar integração para novos sites de notícias e diferentes pós processamentos eles são Factory, Command.

* **Factory** é usado para encapsular a configuração de uma classe NewsScraper para um site de notícias específico. Isso é necessário pois diferentes sites possuem diferentes layouts, fazendo com que seja necessário diferentes configurações para extrair a informação correta.

* **Command** é utilizado para encapsular queries que são feitas para o DOM. Dessa forma é possível adicionar objetivos único e diferentes para cada query sem que o DOMParser se responsabilize por isso. Já que diferentes sites possuem diferentes layouts.

## Como extender mais sites de notícia:
* Criar um novo módulo em `Websites/sitedenotícia`
* Criar uma nova classe em `Websites/sitedenotícia/sitedenoticia_factory` que implementa `ABCNewsScrapperFactory`
* Criar uma nova classe em `Websites/sitedenotícia/sitedenoticia_queries` que implementa `Query` de `Scrapper/abc/ABCQuery`
* Adicionar sua nova factory em `Websites/ConfigureWebsite.py`


## Como incluir novos algorítmos de pós-processamento:
* Criar um novo módulo em `Writer/SeuNovoAlgoritmo`
* Criar uma nova classe em `Writer/SeuNovoAlgoritmo/SeuAlgoritmo` que implementa `ABCWriter` de `Writer/`
* Adicionar seu novo algoritmo em `Writer/ConfigureWriter`
