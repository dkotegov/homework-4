pip3 install -r requirements.txt
sh node.sh 2> /dev/null &
sh grid.sh 2> /dev/null &
python3 run_test.py
