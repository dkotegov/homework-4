# Домашнее задание №4
Нужно написать автоматизированные функциональные тесты по чек-листу, который вы делали в предыдущем задании.
Работа выполняется в командах. На одного человека один чек-лист.

## Команда
**Проект Фото**  
*Данный чек-лист выполнил Кирьяненко Александр*

- Кирьяненко Александр
- Куклина Нина
- Черкасов Кирилл
- Парпибаев Артур

## Требования:
- python 2.7, selenium, chrome, firefox
- все тесты должны запускаться одной командой, а именно ./run_tests.py (заглушка уже есть в репозитории)
- все тесты должны проходить
- не должно быть антипаттернов тестирования
- использование паттерна PageObject
- логин и пароль в тесты нужно передавать через переменные окружения LOGIN и PASSWORD, в коде не должен быть указан пароль.
- запуск через selenium grid и прохождение в firefox, chrome, имя
браузера находится в переменной окружения BROWSER (это либо CHROME, либо FIREFOX)

## Чек-лист
1. Создать альбом
2. Удалить альбом
3. Изменить название у альбома
4. Добавить "класс" к альбому
5. Отмена "класса" у альбома
6. Добавить фото к альбому
7. Добавить фото с описанием  к альбому
8. Добавить "класс" к фото
9. Отмена "класса" у фото
10. Сделать фото обложкой альбома

## Полезные ссылки:
Бинарник selenium (версия 3.11.0): http://selenium-release.storage.googleapis.com/index.html?path=3.11/
Бинарник geckodriver: https://github.com/mozilla/geckodriver/releases
Бинарник chromedriver: http://chromedriver.storage.googleapis.com/index.html?path=2.38/
Пример из лекции (в примере chromedriver и geckodriver для MacOS): https://github.com/dkotegov/tech-testing-selenium-demo

### Запуск ноды:
    java -Dwebdriver.chrome.driver="./chromedriver" -Dwebdriver.gecko.driver="./geckodriver" -jar selenium-server-standalone-3.11.0.jar -role node -hub http://localhost:4444/grid/register -browser browserName=chrome,maxInstances=2 -browser browserName=firefox,maxInstances=2

### Запуск хаба:
    java -jar selenium-server-standalone-3.11.0.jar -role hub
