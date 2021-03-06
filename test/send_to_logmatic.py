import logging
import sys
import socket

sys.path.append('logmatic/')
import logmatic

logger = logging.getLogger()

handler = logmatic.LogmaticHandler("<your_api_key>")
handler.setFormatter(logmatic.JsonFormatter(extra={"hello": "world","hostname":socket.gethostname()}))

logger.addHandler(handler)
logger.setLevel(logging.INFO)

test_logger = logging.getLogger("test")
test_logger.info({"special": "value", "run": 12})
test_logger.info("classic message", extra={"special": "value", "run": 12})

def exception_test():
    try:
        raise Exception('test')
    except Exception:
        test_logger.exception("This is a fake exception")

exception_test()
