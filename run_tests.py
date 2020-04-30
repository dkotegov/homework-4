import subprocess
import os
from time import sleep

import pytest

LINUX = 'linux'
MAC = 'mac'

if __name__ == '__main__':
    subprocess.call("./scripts/run-hub.sh&", shell=True)
    sleep(5)
    operation_system = os.environ.get('os')
    if operation_system == LINUX:
        subprocess.call("./scripts/run-node-mac.sh &", shell=True)
    else:
        subprocess.call("./scripts/run-node-mac.sh &", shell=True)
    sleep(5)
    pytest.main()
