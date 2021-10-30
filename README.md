# E2E тесты ykoya.ru

Запуск тестов на Mac OS:
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
./grid
```

* во втором терминале запускаем selenium node
```shell
./node
```

* в третьем терминале запускаем тесты
```shell
python3 run_tests.py
```