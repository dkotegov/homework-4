import subprocess

import pytest

if __name__ == '__main__':
    subprocess.call("./scripts/run-hub.sh&", shell=True)
    subprocess.call("./scripts/run-node-linux.sh&", shell=True)
    pytest.main()
