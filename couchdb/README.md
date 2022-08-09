# Добро пожаловать в CouchDB ODM!

> Time to relax

## Установка

Актуальную версию CouchDB можно скачать [здесь](https://couchdb.apache.org/#download "Официальный сайт CouchDB").
На данный момент ODM совместима только с CouchDB версии **3.2.0** или выше

## Начало работы

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