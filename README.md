# E2E тесты [ykoya.ru](https://ykoya.ru)

## Запуск тестов на Mac OS:
* устанавливаем venv
```shell
python3 -m venv venv
```

* активируем venv
```shell
source venv/bin/activate
```

* устанавливаем зависимости
```shell
pip3 install -r requirements.txt
```

* устанавливаем [jre](https://www.java.com/ru/download/)

* в первом терминале запускаем selenium hub
```shell
./grid.sh
```

* во втором терминале запускаем selenium node
```shell
./node.sh
```

* в третьем терминале запускаем тесты
```shell
python3 run_tests.py
```

## ENV
Для работы тестов в корне проекта должен находится файл **.env**

В этом файле будут перечислены настройки тестов:
* LOGIN - телефон тестового пользователя
* PASSWORD - пароль тестового пользователя
* USER_ID - ID тестового пользователя 
* BROWSER - в каком браузере запускать тесты (CHROME или FIREFOX)