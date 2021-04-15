## Запуск тестового окружения:

Для запуска может потребоваться дать файлам доступ на исполнение
(chmod 744 grid.sh и chmod 744 node.sh)

`./grid.sh` – запуск selenium

`./node.sh` – запуск chromedriver и geckodriver

## Запуск самих тестов

```
EMAIL=<email> PASSWORD=<password> python ./run_tests.py
``` 