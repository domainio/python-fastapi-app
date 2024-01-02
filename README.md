# Python FastAPI sample app
## Books API app
### Setup
```
python -m venv .venv
source .venv/bin/activate 
pip install -r requiments.txt
```
### :rocket: Launch app
```
uvicorn main:app --reload
```
:white_check_mark: Expectted result:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```


> [!TIP]
> FastAPI automatically generate OpenAPI and Swagger documentation for your API at
> ```http://127.0.0.1:8000/docs```

### Database
This app uses `docker-compose` for local Postgres Database container.   
Just prompt: `docker-compose up` then `docker-compose down` to cleanup.   

The local Postgres docker instansiate with default credetials and db name:
```
username=postgres
password=postgres
database=postgres
```

### Test the API
#### Create a new book (saved into the local DB)
```
curl --location --request POST 'localhost:8000/book/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "book": {
        "title": "Python coding with FastAPI",
        "number_of_pages": 5
    },
    "author": {
        "first_name": "Erez",
        "last_name": "Zohar"
    }
}'
```
#### Get book by ID
```
curl --location --request GET 'localhost:8000/book/{book-id}'
curl --location --request GET 'localhost:8000/book/1'
```
