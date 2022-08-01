#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# async task. program exists before the task is finished

from q1c import q1_task

t = q1_task.s("sample")

robj = t.delay()

print(robj)

