
# FastAPI Clean Architecture Project

This project is a FastAPI application developed using the Clean Architecture principles. It follows a modular structure with four main layers: Model, Storage, Business, and Transport.

## Clean Architecture

Clean Architecture is a software design pattern that promotes separation of concerns and decoupling of dependencies. It allows for better maintainability, testability, and flexibility of the application. The key idea behind Clean Architecture is to create a clear separation between the business rules and the technical implementation details.

## Project Structure

The project structure is organized into modules, and each module consists of the following four main layers:

### 1. Model

The Model layer defines the data structures and entities used within the application. It represents the core business logic and contains the domain-specific models and objects. This layer should be independent of any external frameworks or libraries.

### 2. Storage

The Storage layer is responsible for handling data storage and retrieval. It encapsulates the interaction with databases, file systems, external APIs, or any other external data sources. This layer abstracts away the details of the underlying storage implementation and provides interfaces for data access.

### 3. Business

The Business layer contains the use cases and business logic of the application. It coordinates the interactions between the Model and Storage layers to implement the desired functionality. This layer should be agnostic of the specific data storage or transport mechanisms.

### 4. Transport

The Transport layer handles the communication between the application and the outside world. It includes the APIs, user interfaces, or any other means of interacting with the system. In this project, we are using FastAPI as the web framework for building the API endpoints.

## Getting Started

To run the FastAPI Clean Architecture project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/haiconmeo/fastapi-clean-architecture.git`
2. Navigate to the project directory: `cd fastapi-clean-architecture`
3. Install lib : 

    poetry shell
    poetry install


6. Start the FastAPI server: `uvicorn app.main:app --reload` or python run.py
7. Open your browser and visit `http://localhost:8000/docs` to access the API documentation and explore the available endpoints.


## CLI (Command-Line Interface)

The project includes a CLI (Command-Line Interface) for creating new modules. To create a new module, follow these steps:

Open a terminal or command prompt.
Navigate to the project directory.
Run the following command:
bash
Copy code

    python3 cli/cli.py module_name

## Install library

    poetry config virtualenvs.in-project true
    poetry install

## pgadmin

    pip3 install psycopg2-binary

## Active library

    poetry shell

## Run migrations

    alembic upgrade head

## Initial data

    python ./app/initial_data.py

## Start

    uvicorn app.main:app --reload

If you created a new model in `app/db_model`, 
that imports all the models will be used by Alembic.

After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

    alembic revision --autogenerate -m "Add customm"


## Conclusion

The FastAPI Clean Architecture project provides a solid foundation for developing scalable and maintainable web applications. The use of Clean Architecture principles ensures a clear separation of concerns and facilitates easy testing and extensibility. By following the modular structure with four distinct layers, this project enables efficient development and enhances code organization and reusability.
    curl -sSL https://install.python-poetry.org | python3 -
    or
    pip install poetry

