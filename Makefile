.PHONY: help build run run-db cli
.DEFAULT_GOAL := help

help:				## Prints help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run:				## Runs the app
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
run-dev:				## Runs the app
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
run-db:				## Runs the app
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d postgresql
build:				## Builds docker images
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
build-dev:				## Builds docker images
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml build
cli:				## Entrypoint to web app (helps with Django 'python3 manage.py cmd')
	docker-compose -f docker-compose.yml run --rm --entrypoint /bin/bash web
requirements:       ## export requirements from poetry
	poetry export --format=requirements.txt > app/requirements.txt

