#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from q2worker import q2_task_wc, q2_task_sent, q2_task_para
from celery import group, chain
from helper import longtext, tsprint

t1 = q2_task_wc.s(longtext())
t2 = q2_task_sent.s()
t3 = q2_task_para.s()

ch = chain([t1, t2, t3])

robj = ch()

print(robj)
tsprint("Results before")
print(robj.get())
tsprint("Results after")
