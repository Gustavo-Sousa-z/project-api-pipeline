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
