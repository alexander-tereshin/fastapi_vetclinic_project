# FastAPI Dog API
A simple FastAPI application for managing a list of dogs. This project serves as a homework assignment for the ML and High Load Systems course at the Higher School of Economics.


Features
---
* **Create Dogs** - Add new dog records to the database with a unique primary key (pk).

* **Read Dogs** - Retrieve a list of all dogs or get dogs filtered by their kind.

* **Update Dogs** - Modify an existing dog record by specifying its primary key (pk).

* **Generate Timestamps** - Create and retrieve new timestamp records with unique IDs.

Requirements
---

* Python 3.9+
* FastAPI
* Uvicorn (for running the FastAPI application)
  
Installation
----
1. Clone the repository:

```bash
$ git clone https://github.com/alexander-tereshin/fastapi-dog-api.git
```
2. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

Usage
---

Run the FastAPI application using Uvicorn:

```bash
$ uvicorn main:app --reload
```

API Endpoints
---

* **GET /dog** - Get a list of all dogs or filter by kind.
* **POST /dog** - Create a new dog record.
* **GET /dog/{pk}** - Get a dog by its primary key (pk).
* **PATCH /dog/{pk}** - Update a dog record by its primary key (pk).
* **POST /post** - Generate and retrieve new timestamp records.
  
For more details about the API endpoints and the request/response formats, refer to the Swagger documentation provided when you run the application.

License
---
This project is licensed under the terms of the MIT license.
