#!/usr/bin/env python3 

from celery import Celery
from helper import tsprint

import datetime
import time

BROKER = 'redis://localhost:6379/0',
BACKEND = 'redis://localhost:6379/0'

app = Celery('queue', broker=BROKER, backend=BACKEND)

@app.task(bind=True)
def q1_task(self, in_data):
    print(f"WORKER GOT: {in_data}")
    time.sleep(3)
    print(f"WORKER END {in_data}")
    r = f"{in_data}.{datetime.datetime.now()}"
    return r
