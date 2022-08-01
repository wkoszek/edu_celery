import datetime
def tsprint(v):
	print(f'{datetime.datetime.now()} {v}')
def longtext():
	return '''
	Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.

	It’s a task queue with focus on real-time processing, while also supporting task scheduling.

	Celery has a large and diverse community of users and contributors, you should come join us on IRC or our mailing-list.

	Celery is Open Source and licensed under the BSD License.
	'''
def shorttext():
	return '''
	Celery is Open Source and licensed under the BSD License.
	'''
