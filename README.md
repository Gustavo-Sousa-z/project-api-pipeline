# A ideia deste projeto é combinar diferentes tecnologias.

## Os passos são os seguintes

**A documentação da API esta no diretório [application](https://github.com/Gustavo-Sousa-z/project-api-pipeline/tree/master/application)**

1. Utilizar uma REST API com três rotas (endpoints):

   - **/users** para retornar todos os usuários (GET)

   - **/user/CPF** para retornar um usuário específico (GET)

   - **/user** para registrar um novo usuário (POST)

2. Persistir dados em um Banco de Dados. **Neste projeto foi utilizado MongoDB**

3. Configurar a aplicação para rodar dentro de um Docker container (Dockerfile).

4. Criar um docker-compose para compor a API juntamente com o banco de dados (ambiente de desenvolvimento).

5. Escrever testes unitários para as rotas.

6. Utilizar um Makefile para automatizar os passos mais comuns.

7. Fazer o deploy da aplicação em alguma plataforma de PaaS (Heroku).

8. Criar uma pipeline de CI/CD utilizando alguma ferramenta “as a service” (GitHub Actions, Azure DevOps, etc…). **Neste projeto utilizei github actions**

#### Sinta-se à vontade para adaptar isso para outras linguagens de programação, outras ferramentas, ou até mesmo estender o projeto se quiser.

> Importante instalar:

- Docker

- Python

- VSCode

- Insomnia ou Postman

- Heroku CLI

# Makefile

O Arquivo Makefile contém todos os comandos préviamente configurados para utilizar na pipeline como:

1. **Make test**
   - Comandos para rodar os teste de flake8 e pytest
2. **Make compose-up || compose down**
   - Comandos para testar localmente a API subindo tanto o mongo quanto a API, e limpando os volumes desnecessários
3. **Make Heroku**
   - Comando necessários para autenticar no Heroku, buildar, publicar a aplicação.

# MongoDB

Neste laboratório foi utilizado o free tier do mongodb atlas, conforme explicado [nessa documentação](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/).

Você pode optar por utilizar outras distribuições ou até mesmo outro provedores hospedando na AWS, Azure ou GCP por exemplo.
