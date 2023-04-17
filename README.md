## TP-1 da disciplina de Banco de Dados.

- Objetivo deste trabalho prático é projetar e implementar um banco de dados sobre produtos vendidos em uma loja de comércio eletrônico, incluindo avaliações e comentários de usuários sobre estes produtos. O trabalho consiste na criação de um Banco de Dados Relacional contendo dados sobre compras de produtos e elaboração de um Dashboard, um painel para monitoramento dos dados de compra, gerando uma série de relatórios.

- Dados de entrada será o “Amazon product co-purchasing network metadata” que faz parte do Stanford Network Analysis Project (SNAP).

## Sobre a documentação

Na pasta [documentation](documentation/) conterá três arquivos:

- [INSTRUCTIONS](documentation/INSTRUCTIONS.md): Contém informações mais detalhadas sobre as instalações necessárias para rodar a aplicação, comandos extras que podem ser bastantes úteis e alguns comandos do PostgreSQL.

- [requirements](documentation/requirements.txt): Contém as depêndencias de de bibliotecas necessárias para baixar via pip install no ambiente virtual python criado.

- [tp1_3.1](documentation/tp1_3.1.pdf): Contém a documentação solicitada no item 3.1 do TP1, onde tem um diagrama correspondendo ao esquema do Banco de Dados Relacional, observando as diretrizes da Seção 6, além de um dicionário de dados descrevendo cada relação, atributo, restrição de integridade referencial ou de outro tipo que
fizer parte do esquema do banco de dados.

## Sobre os Scripts

Na pasta [scripts](scripts/) conterá todos os scripts utilizados para a elaboração da aplicação, segue abaixo uma breve descrição sobre cada script:

- [amazon-meta-sample.txt](scripts/amazon-meta-sample.txt): contém uma pequena parte dos dados de entrada do arquivo principal (amazon-meta.txt) com o intuito de realizar testes da aplicação de forma mais rápida, ao invés de carregar o arquivo "amazon-meta.txt" inteiro com todos os 548.552 produtos.

- [database.ini](scripts/database.ini): é um arquivo de configuração para armazenar todos os parâmetros de conexão com o banco de dados.

- [config.py](scripts/config.py): lê o database.ini e retorna os parâmetros da conexão com o banco de dados.

- [connect.py](scripts/connect.py): se conecta ao banco de dados passado no arquivo database.ini (o banco de dados já tem que estar criado) e imprime a versão do banco de dados PostgreSQL.

- [create_database.py](scripts/create_database.py): cria um banco de dados, no nosso caso, o banco de dados 'amazon'.

- [create_tables.py](scripts/create_tables.py): cria as tabelas do banco de dados.

- [drop_database.py](scripts/drop_database.py): exclui o banco de dados inteiro. Esse script foi criado com o propósito de facilitar a exclusão do banco de dados todo quando estávamos realizando testes, ao invés de excluir as linhas de cada tabela no banco de dados, pois dessa forma demorava muito.

- [insert.py](scripts/insert.py): povoa as tabelas do banco de dados.

- [read_file.py](scripts/read_file.py): realiza a extração dos dados do arquivo de entrada.

- [sql_queries.py](scripts/sql_queries.py): contém todos os comandos SQL implementados para realizar as consultas descritas na seção 7.

- [tp1_3.2.py](scripts/tp1_3.2.py): realiza a extração dos dados do arquivo de entrada, criação do esquema do banco de dados, e povoamento das
relações com estes dados, conforme descrito no item 3.2.

- [tp1_3.3.py](scripts/tp1_3.3.py): é a implementação do Dashboard, onde o usuário poderá executar todas as consultas descritas na seção 7.

## Aviso Importante

No script [tp1_3.2.py](scripts/tp1_3.2.py), verifique se você está passando o nome do arquivo de entrada corretamente e se o arquivo de entrada está no diretório correto para que o script rode corretamente sem erros!

```sh
    filename = 'amazon-meta.txt'
```

Caso não possua o arquivo de entrada, baixe clicando no link [amazon-meta](https://snap.stanford.edu/data/amazon-meta.html).
