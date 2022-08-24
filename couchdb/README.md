# Добро пожаловать в CouchDB ODM!

> Time to relax

## Установка

Актуальную версию CouchDB можно скачать [здесь](https://couchdb.apache.org/#download "Официальный сайт CouchDB").
На данный момент ODM совместима только с CouchDB версии **3.2.0** или выше

## Подготовка

CouchDB — NoSQL база данных, поэтому традиционные SQL-запросы для неё бесполезны.
Взаимодействие происходит через REST API.

После установки, убедитесь, что CouchDB работает:

```shell
curl -X GET http://localhost:5984/
```

Ответ должен выглядеть примерно так (зависит от версии):
>{"couchdb": "Welcome",  
> "version": "3.0.0",  
> "git_sha": "83bdcf693",  
> "uuid": "56f16e7c93ff4a2dc20eb6acc7000b71",  
> "features": [  
>     "access-ready",  
>     "partitioned",  
>     "pluggable-storage-engines",  
>     "reshard",  
>     "scheduler"  
> ],  
> "vendor": {  
>     "name": "The Apache Software Foundation"  
>     }  
> }


Список всех баз данных, находящихся в CouchDB, можно получить следующим запросом:

```shell
curl -X GET http://<username>:<password>@localhost:5984/_all_dbs
```
Где username и password — соответственно, логин и пароль для входа

Также вы можете воспользоваться веб-версией интерфейса CouchDB, под названием Project Fauxton.
Она находится по адресу http://localhost:5984/_utils

В случае, если при установке вы указали другие значения для хоста и порта, замените
**localhost** и **5984** в ссылках на ваши значения.


## Начало работы

Создайте экземпляр класса Couch, который позволит взаимодействовать с CouchDB:

```python
import couchdb

server = couchdb.Couch(db_host="<your_host>", db_port="<your_port>")
```

"localhost" и 5984 — значения по умолчанию для db_host и db_port соответственно

### Авторизация

У вас есть два способа создать авторизированную сессию CouchDB:

* Передать экземпляр класса DatabaseUser в конструктор
```python
import couchdb
from models import DatabaseUser

user = DatabaseUser(username="DB_USERNAME", password="DB_PASSWORD")
server = couchdb.Couch(user=user)
```

* Авторизоваться позже, используя метод authorize:
```python
server.authorize(username="DB_USERNAME", password="DB_PASSWORD")
```


## Работа с базами данных

### Создание или получение базы данных

Создать новую или получить существующую базу данных можно с помощью класса Couch
```python
database = server.get_or_create_db("DB_NAME")
```

### Запись в базу

Для того чтобы создать запись в базе данных, нужно создать экземпляр класса Document 
и передать его в метод create_document. В конструктор Document пары ключ-значение 
передаются в виде именованных аргументов
```python
import couchdb

server = couchdb.Couch()
database = server.get_or_create_db("DB_NAME")
document = couchdb.Document(arg1="foo", arg2="bar", arg3=42)
database.create_document(document)
```

