APP = restapi-dev # Declarando a variavel que será chamada nos comandos abaixo

test:
	@flake8 . --exclude .venv
	#@pytest -v --disable-warnings

compose-up:
	@docker-compose build
	@docker-compose up -d

compose-down:
	@docker compose down
	@docker volume prune -f --filter="label!=name=projeto-api-flask_db_data"

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web