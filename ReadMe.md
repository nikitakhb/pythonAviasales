# Aviasales Case v0.91
Версия кейса решенная на python 3.8 без фреймворков.

Запустить контейнер
```shell script
docker-compose up --build
```
Контейнер запустится на ```8000``` порту.

Иструкция по использованию сервиса:
```
1. curl localhost:8000/load -d '["foobar", "aabb", "baba", "boofar", "test"]' 
2. curl localhost:8000/get?word='foobar'
```
Описание эндпоинтов:
* /load - эндпоинт принимающий POST запросы. Принимает список слов, которые хранит до перезаписи списка.
* /get?word= - эндпоинт принимающий GET запросы. Принимает параметр ```word``` возвращает аннаграммы
 слова из заранее загруженного словаря.