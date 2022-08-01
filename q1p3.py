#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from q1worker import q1_task
from celery import group

t1 = q1_task.s("sample 1")
t2 = q1_task.s("sample 2")
t3 = q1_task.s("sample 3")

g = group([t1, t2, t3])

robj = g()

print(robj)
