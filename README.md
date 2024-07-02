# A ideia deste projeto é combinar diferentes tecnologias.

## Os passos são os seguintes

1. Utilizar uma REST API com três rotas (endpoints):

   - **/users** para retornar todos os usuários (GET)

   - **/user/CPF** para retornar um usuário específico (GET)

   - **/user** para registrar um novo usuário (POST)

2. Persistir dados em um Banco de Dados. \*\*Neste projeto foi utilizado

3. Configurar a aplicação para rodar dentro de um Docker container(Dockerfile).

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
