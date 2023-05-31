# Instalação e configuração do ambiente

## Pré-requisitos

- Python 3.8 ou superior

## Instalação

1. Clone o repositório:

```
git clone https://github.com/nicolasgaldino/controle-de-visitantes
```

2. Crie um ambiente virtual:

```
python -m venv nome-do-ambiente
```

3. Ative o ambiente virtual:

```
source nome-do-ambiente/bin/activate  # Linux/MacOS
nome-do-ambiente\Scripts\activate  # Windows
```

4. Instale as dependências:

```
pip install -r requirements.txt
```

## Dependências

As seguintes dependências foram utilizadas na versão atual do projeto:

| Dependência                | Versão    |
|----------------------------|-----------|
| asgiref                    | 3.7.2     |
| Django                     | 4.2.1     |
| django-widget-tweaks       | 1.4.12    |
| flake8                     | 6.0.0     |
| mccabe                     | 0.7.0     |
| mypy                       | 1.3.0     |
| mypy-extensions            | 1.0.0     |
| pycodestyle                | 2.10.0    |
| pyflakes                   | 3.0.1     |
| sqlparse                   | 0.4.4     |
| tomli                      | 2.0.1     |
| typing_extensions          | 4.6.2     |

## Inicializando o Projeto

Depois de instalar as dependências, você deve executar os seguintes comandos no terminal para ativar o servidor local:

1. Acesse a pasta raiz do seu projeto Django:

```
cd /caminho/para/o/projeto
```

2. Execute o seguinte comando para rodar as migrações do banco de dados:

```
python manage.py migrate
```

3. Por fim, execute o comando para iniciar o servidor local:

```
python manage.py runserver
```
