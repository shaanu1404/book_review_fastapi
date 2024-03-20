### Setup

- Create a virtual environment and activate

```bash
pip -m venv <env_name>
source bin/activate
```

- Install required dependencies added in **requirements.txt**

```bash
pip install -r requirements.txt
```

- Run app using command

```bash
uvicorn book_review_app.main:app --reload
```

- Go to api docs [API DOCS](http://localhost:8000/docs)

### Theory

- Question 1: Explain how FastAPI handles asynchronous requests and its
  benefits over synchronous code in Python.

      FastAPI uses *asyncio* library internally. FastAPI uses the Starlette web framework which is built on top of the asyncio library for python.
      Therefore, user can define route handler using the syntax 'async def' which will do the handling of the api requests and other asynchronous tasks like i/o, network, etc. efficiently.

      This provides some benefits like asynchronous database queries, concurrency on a single thread, non blocking i/o which takes care of multiple requests concurrently, etc. This gives overall improved performance of the api.

- Question 2: Describe how dependency injection works in FastAPI and give an
  example of its practical use.

      In FastAPI, the dependencies are passed as parameters to the api route handler function automatically. This is called dependency injection. This allows us to define the required dependecies of the handler in the arguments itself and use it efficiently without any manual configuration. These dependencies can be database, sessions, queries, authentication headers, etc.

      We can define functions that return the required dependency object and pass that function reference to the handler. The fastAPI executes the dependency function when the endpoint is hit and injects the dependency in the handler. Thus, providing the required objects to function. It also manages the lifecycle of the dependency injected.

- Question 3: Code walkthrough

  - The main entry point of the application is the book_review_app/main.py file. It implements the fastAPI server and define and handles the routes. You can run the api using the main.py file
    `uvicorn book_review_app.main:app --reload`
  - The file database.py configures the SQLAlchemy library for handling sqlite database.
  - The models.py file contains the database table models, here, the Book and the Review models.
  - The schemas.py file contains the pydantic models for the api endpoint data. It also provides the basic types and validation for the route arguments.
  - The task.py file contains a dummy function which serves as a background task. When a new review is added it adds a log to the file named 'email_confirmation.txt'.
  - The test_main.py contains few test for testing the api endpoint.
