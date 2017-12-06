# Selenium Tests for ok.ru
## Чеклист
- открытие окна обсуждений
- открытие таба мои заметки
- открытие таба участвовал
- открытие таба группы
- создание своей заметки
- комментирование своей заметки
- удаление комментария своей заметки
- изменение комментария своей заметки
- отправка сообщения
- открытие таба заметки друзей
- нажатие на "звонок" открывает модальное окно звонка
- нажатие на кнопку завершенияя звонка завершает звонок
- работает кнопка вкл/выкл камеры
- работает кнопка вкл/выкл микрофона
- работает кнопка перезвонить
- при нажатии на имя собеседника справа появляется информация о пользователе
- при введениии в инпут поиска появляется список результата поиска
- инпут поиска не реагирует на строку из пробелов
- при нажатии на кнопку "домой" закрывается текущий диалог
- при наведении на имя автора комментария, появляется карточка юзера над курсором
- появляется кнопка "вниз" при скролле истории комментариев вверх
- появляются кнопки "класс", "ответить", "поделиться" при наведении курсора на комментарий
- появляются кнопка "пожаловаться" и время создания при наведении курсора на коммментарий
- появляются кнопка  время создания при наведении курсора на коммментарий

## Downloads
* [Selenium](http://selenium-release.storage.googleapis.com/index.html)
* [Selenium gecko driver](https://github.com/mozilla/geckodriver/releases)
* [Selenium chrome driver](http://chromedriver.storage.googleapis.com/index.html)

## Instructions
### Install
1. Clone this repo
```bash
git clone https://githib.com/ed-asriyan/homework-4
cd homework-4
```

2. Install virtualenv
```bash
pip install virtualenv
```

4. Create virtualenv
```bash
virtualenv .venv
```

5. Install dependencies
```bash
pip install -r requirements.txt
```

6. Download selenium standalone server and unachieve it to it directory (save as `selenium-server-standalone.jar`).
7. Download selenium gecko driver and unachieve it to it directory.
8. Download chrome driver and unachieve it to it directory.

### Run the grid
```bash
./grid.sh
```

### Run a new node
```bash
./node.sh
```
### Run tests
1. Open virtual env
```bash
source .venv/bin/activate
```

2. Run tests
```bash
BROWSER=<browser> LOGIN=<login> PASSWORD=<password> ./run_tests
```
* `browser`: `FIREFOX` or `CHROME`
* `login`: ok.ru login
* `password`: ok.ru password
