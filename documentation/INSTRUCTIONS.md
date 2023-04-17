## Instalações Necessárias

Instalar o docker no WSL2. Para isso, segue o tutorial: [Instalação Docker](https://gitlab.com/paulonellessen/docker-saas/-/wikis/Instalando%20o%20Docker/Ubuntu).

Instalar o PostgreSQL no WSL2, com os seguintes comandos:

```sh
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql postgresql-contrib
```

Caso você usa o Linux, basta seguir os passos:

```sh
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
sudo apt-get -y install postgresql
```

Construir e inicializar todos os contêineres necessários para executar a aplicação (-d para ser executado em segundo plano):

```sh
docker compose up -d
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

Para iniciar o serviço Docker, digite o comando:

```sh
sudo service docker start
```

Para para o serviço Docker, digite o comando:

```sh
sudo service docker stop
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

## Comandos PostgreSQL

Se estiver usando o WSL2 para rodar a aplicação, precisará informar o endereço IP dele. Para obter o endereço IP do WSL2, abra um terminal e execute o seguinte comando:

```sh
ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'
```

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
psql -h localhost -U postgres
```

Para listar todos os banco de dados criados:

```sh
\l
```

Para entrar em um determinado banco de dados, devemos passar ele como parâmetro ao iniciar a sessão interativa com o PostgreSQL.

```sh
psql -h 172.22.70.191 -U postgres amazon
psql -h localhost -U postgres amazon
```

Para listar as tabelas no banco de dados, use o comando:

```sh
\dt
```
