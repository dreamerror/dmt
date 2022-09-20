Выполните в родительской директории:

```shell
docker build -t IMAGE_NAME -f .docker/Dockerfile . 
```

Затем, для запуска контейнера:

```shell
docker run -d -p 8000:8000 IMAGE_NAME  
```