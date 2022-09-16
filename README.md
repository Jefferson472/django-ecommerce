# WIP
Lista de pendências:
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
