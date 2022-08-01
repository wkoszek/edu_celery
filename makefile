# example
w1:
	python3 -m celery -A q1worker worker -l INFO
w2:
	python3 -m celery -A q2worker worker -l INFO
w3:
	python3 -m celery -A q3worker worker -l INFO
clean:
	python3 -m celery -A q3worker purge
