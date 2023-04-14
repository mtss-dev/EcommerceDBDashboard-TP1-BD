## Instalações Necessárias

Instalar o docker no WSL2. Para isso, segue o tutorial: [Instalação Docker](https://gitlab.com/paulonellessen/docker-saas/-/wikis/Instalando%20o%20Docker/Ubuntu).

Baixar as atuualizações mais recentes do repositório:

```sh
git pull
````

Baixar a imagem do docker compose com o PostgreSQL:

```sh
docker compose up
```

Criar um ambiente virtual Python:

```sh
python3 -m venv .tp1
```

Entrar no ambiente virtual:

```sh
source .tp1/bin/activate
```

Instalar a biblioteca psycopg2 (no amnbiente virtual):

```sh
pip install psycopg2-binary
```

Para sair do ambiente virtual, digite o seguinte comando:

```sh
deactivate
```

## Comandos Extras

Para atualizar os pacotes, basta digitar os seguintes comandos:

```sh
sudo apt update
```

```sh
sudo apt upgrade
```

Para listar todos os serviços que estão rodando no WSL2:

```sh
sudo service --status-all
```

Para verificar se já existe algum serviço em execução em uma determinada porta, basta usar o seguinte comando no terminal:

```sh
sudo lsof -i :5432
```

(A porta padrão do PotsgreSQL é a 5432)
Se o comando retornar uma linha de saída, significa que há um processo em execução na porta passada como parâmetro. Nesse caso, você pode encerrar o processo usando o comando:

```sh
sudo kill <PID>
```

Para verificar a porta em que o PostgreSQL está executando no WSL2, você pode usar o comando pg_lsclusters. Basta abrir um terminal e digitar o comando:

```sh
pg_lsclusters
```

Para iniciar o serviço Docker no WSL2, digite o comando:

```sh
sudo service docker start
```

Para parar a execução da aplicação (Docker compose):

```sh
docker compose down
```
Para listar as imagens instaladas no Docker:

```sh
docker images
```

Para listar os containers do Docker:

```sh
docker compose ps
```

Para obter o endereço IP do WSL2, abra um terminal e execute o seguinte comando:

```sh
ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'
```

## Scripts Python

O database.ini é um arquivo de configuração para armazenar todos os parâmetros de conexão com o banco de dados.
O arrquivo config.py lê o database.ini e retorna os parâmetros da conexão com o banco de dados.
O arquivo connect.py se conecta ao banco de dados passado no arquivo database.ini (o banco de dados já tem que estar criado) e imprime a versão do banco de dados PostgreSQL.

Os arquivos create_table.py, insert.py e update.py são autoexplicativos. Neles contém exemplos de como podemos efetuar essas operações em um banco de dados genericos (suppliers).

## Comandos PostgreSQL

O comando psql é usado para iniciar uma sessão interativa com o PostgreSQL. O parâmetro -h especifica o host do servidor ao qual deseja se conectar e o parâmetro -U especifica o nome do usuário que está iniciando a sessão.

```sh
psql -h 172.22.70.191 -U postgres
```

No comando psql -h 172.22.70.191 -U postgres, estamos tentando se conectar ao servidor que está localizado no endereço IP 172.22.70.191 (o endereço IP do seu WSL2 pode ser diferente, se for, substitua pelo seu) com o usuário postgres.

Ou excecute tudo isso em apenas uma linha no terminal:

```sh
psql -h $(ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}') -U postgres
```

Se você usa Linux, basta digitar:

```sh
psql -h 172.22.70.191 -U postgres
```

Para listar todos os banco de dados criados:

```sh
\l
```

Para entrar em um determinado banco de dados, devemos passar ele como parâmetro ao iniciar a sessão interativa com o PostgreSQL.

```sh
psql -h 172.22.70.191 -U postgres suppliers
```

Onde "suppliers" é um banco de dados genérico de exemplo.

Para listar as tabelas no banco de dados, use o comando:

```sh
\dt
```

Por padrão, o PostgreSQL inicia um serial em 1,2,3,4...
Para começar em 0, segue o exemplo:

```sh
        CREATE SEQUENCE vendor_id_seq
            START WITH 0
            INCREMENT BY 1
            MINVALUE 0
            NO MAXVALUE
            CACHE 1;
        CREATE TABLE vendors (
            vendor_id INTEGER DEFAULT NEXTVAL('vendor_id_seq') PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
```

