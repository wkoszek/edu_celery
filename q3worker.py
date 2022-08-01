#!/usr/bin/env python3 

from celery import Celery
from helper import tsprint

import datetime
import time

BROKER = 'redis://localhost:6379/0',
BACKEND = 'redis://localhost:6379/0'

app = Celery('queue', broker=BROKER, backend=BACKEND)

@app.task(bind=True)
def q3_task_wc(self, in_data):
    print(f"WORKER GOT: {in_data}")
    time.sleep(3)
    ret = len(in_data.split(" "))
    print(f"WORKER END {in_data} -> {ret}")
    return in_data + f'\nWords: {ret}'

@app.task(bind=True)
def q3_task_sent(self, in_data):
    print(f"WORKER GOT: {in_data}")
    time.sleep(3)
    ret = len(in_data.split("."))
    print(f"WORKER END {in_data} -> {ret}")
    return in_data + f'\nSent: {ret}'

@app.task(bind=True)
def q3_task_para(self, in_data):
    print(f"WORKER GOT: {in_data}")
    time.sleep(3)
    ret = len(in_data.split("\n\n"))
    print(f"WORKER END {in_data} -> {ret}")
    return in_data + f'\nPara: {ret}'

@app.task(bind=True)
def q3_task_wait(self, s):
    print(f"WORKER GOT: {s}")
    time.sleep(s)
    print(f"WORKER END {s}")
    return s

@app.task(bind=True)
def q3_task_print(self, s):
    print(f"PRINT {s}")
    return s
