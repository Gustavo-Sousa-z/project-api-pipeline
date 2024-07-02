# A ideia deste projeto é combinar diferentes tecnologias.

## Os passos são os seguintes

1. Utilizar uma REST API com três rotas (endpoints):

   - **/users** para retornar todos os usuários (GET)

   - **/user/CPF** para retornar um usuário específico (GET)

   - **/user** para registrar um novo usuário (POST)

2. Persistir dados em um Banco de Dados. **Neste projeto foi utilizado MongoDB**

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

# API Documentation

## Endpoints

### 1. Get All Users

**URL:** `/users`

**Method:** `GET`

**Description:** Retrieve all users.

**Responses:**

- **200 OK:** Returns a list of users.

### 2. Get User by CPF

**URL:** `/user/<string:cpf>`

**Method:** `GET`

**Description:** Retrieve a user by their CPF.

**Parameters:**

- **cpf** (string, required): The CPF of the user.

**Responses:**

- **200 OK:** Returns the user data.
- **400 Bad Request:** The user does not exist.

### 3. Create User

**URL:** `/user`

**Method:** `POST`

**Description:** Create a new user.

**Parameters:**

- **first_name** (string, required): The first name of the user.
- **last_name** (string, required): The last name of the user.
- **cpf** (string, required): The CPF of the user.
- **email** (string, required): The email of the user.
- **birth_date** (string, required): The birth date of the user.

**Responses:**

- **200 OK:** User created successfully.
- **400 Bad Request:** Invalid CPF or CPF already exists in the database.

## Models

### UserModel

**Fields:**

- **first_name** (string, required)
- **last_name** (string, required)
- **cpf** (string, required, unique)
- **email** (string, required)
- **birth_date** (string, required)
