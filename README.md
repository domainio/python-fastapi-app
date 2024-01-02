# Python FastAPI sapmle app
## Books API app
### Setup instructions
```
python -m venv .venv
source .venv/bin/activate 
pip install -r requiments.txt
```
### :rocket: Launch app
```
uvicorn books-api.main:app --reload
```
:white_check_mark: Expectted result:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```


> [!TIP]
> FastAPI automatically generate OpenAPI and Swagger documentation for your API at
> ```http://127.0.0.1:8000/docs```

You may use local Postgres Database with this `docker-compose.yaml` file:
```
version: '3'

services:
  postgresql:
    image: docker.io/bitnami/postgresql:16
    ports:
      - '5432:5432'
    volumes:
      - 'postgresql_data:/bitnami/postgresql'
    environment:
      - 'ALLOW_EMPTY_PASSWORD=yes'
volumes:
  postgresql_data:
    driver: local
```
Locate the file in the app directory and just prompt: `docker-compose up` then `docker-compose down` to cleanup.   

The local Postgres docker instansiate with default credetials and db name:
```
username=postgres
password=postgres
database=postgres
```