# Подготовка

## Подготовка скриптов

Разрешить скрипты на выполнение  
`chmod +x start_*.sh`

## Подготовка окружения python
- Проверьте версию питона (у нас минимальная 3.6.9)

- Инициализировать и активировать окружение  
`python3 -m venv env && source env/bin/activate`

- Установите все зависимости  
`pip install -r requirements.txt`

- Если вы использете PyCharm, возможно, придётся установить окружение в качестве дефолтного для проекта    
 https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment

# Использование
- Запустить selenium grid hub  
`./start_hub.sh`

- Запустить selenium grid nodes  
`./start_nodes.sh`

- Активировать окружение (если работаете через PyCharm, то там окружение само активируется)  
`source env/bin/activate`

- Деактивировать окружение 
`deactivate`

- Запустить все тесты из активированного окружения  
`BROWSER=CHROME LOGIN=my_login PASSWORD=my_password python run_tests.py`

- Запустить определенный test case из активированного окружения 
`BROWSER=CHROME LOGIN=my_login PASSWORD=my_password python -W ignore -m unittest cases.test_login_page.LoginPageTest`

# Дополнительная информация
Не забывайте форматировать код перед коммитом  
`autopep8 .`
