#!/usr/bin/env python3
# vim: set syntax=python:
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# Sync task. Program dispatches a task and .get() will make it wait for
# the result

from q1worker import q1_task

t = q1_task.s("sample")

robj = t.delay()

print(robj)
print(robj.get())
