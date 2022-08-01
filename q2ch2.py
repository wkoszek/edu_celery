#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from q2worker import q2_task_wc, q2_task_sent, q2_task_para
from celery import group, chain
from helper import longtext, tsprint

import sys

t1 = q2_task_wc.si(longtext())
t2 = q2_task_sent.si(longtext())
t3 = q2_task_para.si(longtext())

ch = chain([t1, t2, t3])

robj = ch.delay()

print(robj)

robj.get()

#print(robj.parent.parent.graph.to_dot(sys.stdout)) # fh)
print(robj.graph.to_dot(sys.stdout)) #parent.parent.graph.to_dot(sys.stdout)) # fh)
