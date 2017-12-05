# Selenium Tests for ok.ru
- работает кнопка справки звонка
- уведомления в беседе выключаются
- уведомления в беседе включаются
- смайлики отправляются
## Downloads
* [Selenium](http://selenium-release.storage.googleapis.com/index.html?path=3.7)
* [Selenium gecko driver](https://github.com/mozilla/geckodriver/releases)
* [Selenium chrome driver](http://chromedriver.storage.googleapis.com/index.html?path=2.33)

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
