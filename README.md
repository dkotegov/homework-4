# Подготовка

## Подготовка скриптов

Разрешить скрипты на выполнение  
`chmod +x start_*.sh`

## Подготовка окружения python
- Проверьте версию питона  
Я использую 3.6.9, но думаю, что если версия выше этой, то не страшно

- Инициализировать и активировать окружение
`python3 -m venv env && source env/bin/activate`

- Установите все зависимости  
`pip install -r requirements.txt`

- Если вы использете PyCharm, откройте там проект и
 установите созданное окружение в качестве дефолтного для проекта  
 https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment

# Использование


Запустить selenium grid hub  
`./start_hub.sh`

Запустить selenium grid nodes  
`./start_nodes.sh`

Запустить тесты  
`BROWSER=CHROME python run_tests.py`
