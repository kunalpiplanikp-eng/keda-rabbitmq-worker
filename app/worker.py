import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

while True:
    logging.info("hello world from worker")
    time.sleep(10)