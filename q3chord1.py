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

t1 = q3_task_wc.si(shorttext())
t2 = q3_task_sent.si(shorttext())
t3 = q3_task_para.si(shorttext())

cho = chord([t1, t2, t3])

robj = cho(q3_task_print.s())

print(robj)

robj.get()
