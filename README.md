## How To Run
### Launch hub
```
bash ./hub.sh
```
### Launch node
```
bash ./node.sh
```
### Launch tests
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
LOGIN='testuser' EMAIL='testemail@mail.ru' PASSWORD='testuser1' BROWSER='CHROME' python3 run_tests.py
```
