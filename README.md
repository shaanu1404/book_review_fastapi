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
