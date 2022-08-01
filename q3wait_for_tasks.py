#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# This shows how Celery's chord is blending results from 3 workers in an
# array that is later passed into the chord's callback

from q3worker import q3_task_wc, q3_task_sent, q3_task_para, q3_task_wait, q3_task_print
from celery import group, chain, chord
from helper import longtext, shorttext, tsprint

import sys
import os
import time
import datetime

num_tasks = 1000

print("Submitting tasks")
tids = []
for i in range(0, num_tasks):
	t = q3_task_wait.si(.5).delay()
	tids.append(t)
print("Submission done")

print("Starting WAIT LOOP")
seen = 0
rmed = 0	# sep. counter for rm'ed items so progress report reliable
for wi in range(1,999999):
	for ti, t in enumerate(tids):
		if t.status == "SUCCESS":
			#print(f"REMOVING {ti}")
			del tids[ti]
			seen += 1
			rmed += 1
		if rmed == 100:
			print(f"{seen} tasks done, loop {wi} at {datetime.datetime.now()}")
			rmed = 0
	if seen == num_tasks:
		break
	time.sleep(1)

print("Totally done")
