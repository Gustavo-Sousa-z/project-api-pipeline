APP = restapi-dev

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose-up:
	@docker-compose build
	@docker-compose up

compose-down:
	@docker compose down
	@docker volume prune -a -f

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web