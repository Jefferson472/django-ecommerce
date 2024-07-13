# WIP

<div align="center" id="badges">
    <img src="https://img.shields.io/badge/STATUS-WIP-red"/>
</div>

# Instalando o projeto

1. Clone o repositório:
Abra um terminal e utilize o código abaixo. Se estiver no VSCode, abra uma nova janela selecione para clonar um novo repositório e cole o link, depois é só escolher um local para salvar.
    
    ```
    git clone https://github.com/Jefferson472/django-ecommerce.git
    
    ```
    
2. Inicie um ambiente virtual com o comando abaixo:
    
    ```
    python -m venv venv
    
    ```
    
    Ative o ambiente
    
    ```
    venv/Scripts/activate # Windows
    venv/bin/activate # Linux
    
    ```
    
3. Instale as dependências do projeto com o comando abaixo:
    
    ```
    python -m pip install -r src/requirements-dev.txt
    
    ```
    

## Rodando o projeto

1. Grave as migrates no banco de dados:
    
    ```
    python ./src/manage.py makemigrations
    python ./src/manage.py migrate
    
    ```
    
2. Execute o servidor django com os comandos abaixo:
    
    ```
    python src/manage.py runserver
    
    ```
    

## Criando e Submetendo um Pull Request

Não faça nenhum commit direto na branch main, sempre que fizer uma modificação inicie uma nova branch. Basta seguir os comandos abaixo:

Este comando irá criar uma nova branch e trocar para esta branch:

```
git checkout -b <nome da sua branch>

```

Comentar na branch a esquerda cada uma com suas observações ou:

```
git add . # para add todos os arquivos modificados
git commit -m "seus comentários"

```

Quando finalizar todas alterações vá até o github e clique em abrir pull request.


---
## Lista de pendências:
- verificar traduções que foram automáticas com django translate
- remover a tradução parler de name e slug (não faz sentido para loja de games)
- add senha ao compose redis
- verificar dockercompose rabbit não funciona
- verificar dockercompose celery não funciona
- add recomendação fake quando não houver nenhuma recomendação ou a conexão com redis falhar
- add um try para o celery em caso de falha
- add um try para o redis em caso de falha
- melhorar o CSS (remover o css inútil e refazer)
- escrever um readme melhor
- hospedar o projeto

# django-ecommerce
Projeto de loja online criado com Django


# API de Pagamentos
Link para SandBox Braintree
https://sandbox.braintreegateway.com/login

Cartão de Crédito Braintree retorna Sucesso
card: 4111 1111 1111 1111
cvv: 123
date: 12/28

WeasyPrint
Guia de instalação em caso de erro:
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation


### Comandos para Traduções

Obs.: Se receber erro referente ao gettext pode baixar aqui: 

https://www.gnu.org/software/gettext/ Para Linux

https://mlocati.github.io/articles/gettext-iconv-windows.html Para Windows

```python
django-admin makemessages -l en -l pt_BR
django-admin makemessages --all
```
```python
django-admin compilemessages 
```

### Parler

```python
python src/manage.py makemigrations ecommerce --name "translations"
```

No arquivo migrations existe um erro ao gerar migrate:
```python
bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
```
Substituta em todas as ocorrências:
```python
bases=(parler.models.TranslatableModel, models.Model),
```
