.PHONY: makemigrations migrate s server c console

PM = python manage.py

makemigrations:
	$(PM) makemigrations

migrate:
	$(PM) migrate

server:
	$(PM) runserver
s: server

console:
	$(PM) shell
c: console