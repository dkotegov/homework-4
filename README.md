# Тестики
[Чек лист](http://jira.bmstu.cloud/browse/QA-827) на регистрацию в сервисе [virusmusic.fun](https://virusmusic.fun)

## Запуск
### 1. В отдельном терминале запускаем хаб: `./hub.sh`
### 2. В отдельном терминале запускаем ноду: `./node.sh`
### 3. В отдельном терминале запускаем тесты:  
```bash
LOGIN='mylogin' PASSWORD='qwerty' BROWSER='CHROME' python3 run_tests.py
```
> * LOGIN - тестовый логин, 
> * PASSWORD - пароль от тестового аккаунта,
> * \[BROWSER\] - опциональный параметр, указывающий браузер, в котором тестировать (CHROME или FIREFOX)

### 4. Держим кулачки
иначе не пройдет
