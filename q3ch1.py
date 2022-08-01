#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from q3worker import q3_task_wc, q3_task_sent, q3_task_para, q3_task_wait
from celery import group, chain
from helper import longtext, shorttext, tsprint

import sys
import os

t1 = q3_task_wc.si(shorttext())
t2 = q3_task_sent.si(shorttext())
t3 = q3_task_para.si(shorttext())

t4 = q3_task_wait.si(1.0001)
t5 = q3_task_wait.si(1.0002)
t6 = q3_task_wait.si(1.0003)
g = group([t4, t5, t6])

ch = chain([t1, g, t3])

robj = ch.delay()

print(robj)

robj.get()

with open('./graph.dot', 'w+') as fh:
    robj.parent.parent.graph.to_dot(fh)

os.system('echo hello; dot -Tpng -ograph.png graph.dot; echo world')
