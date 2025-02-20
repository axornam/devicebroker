import sys

if sys.platform == "win32":
    # DEF_SOCK_NAME = "\\\\.\\pipe\\devbroker_54C653E3"
    DEF_SOCK_NAME = "127.0.0.1:8002"
else:
    DEF_SOCK_NAME = "/tmp/devbroker_54C653E3"
