# Projeto Python com SQL

Este projeto utiliza Python e SQL para realizar operações de banco de dados. Abaixo estão as instruções para iniciar o projeto e as configurações necessárias.

## Pré-requisitos

- Python 3.10 ou superior (Recomenda-se utilizar a versão 3.12 em ambiente Windows)
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório para sua máquina local:
    ```sh
    git clone https://github.com/Braiani/login_ctk.git
    cd login_ctk
    ```

2. Crie um ambiente virtual (recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências do projeto:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

1. Configure o banco de dados:
    - Crie um banco de dados SQL.
    - Atualize as configurações de conexão no arquivo `.env` (crie uma cópia a partir do arquivo .env.example disponível).

    Exemplo de configuração:
    ```env
    host='www.db4free.net'
    port='3306'
    database='mercado_senac'
    user='suporte_senac'
    password='sl7oU2hJ0rUl'
    ```
2. Executar o script SQL disponível no arquivo `database.sql` dentro do banco criado/apontado nas configurações anteriores.

## Executando o Projeto

1. Execute o script principal do projeto:
    ```sh
    python3 Main.py
    ```

2. Verifique os logs para garantir que a aplicação está conectada ao banco de dados e funcionando corretamente.