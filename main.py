from fastapi import FastAPI, HTTPException
from . import schemas
from . import database
from . import convertors

app = FastAPI()


@app.get("/")
def get_root():
    return "welcome to books api"


@app.post("/book/")
def create_book(request: schemas.BookAuthorPayload):
    database.add_book(convertors.convert_into_book_db_model(request.book),
                      convertors.convert_info_author_db_model(request.author))
    return f"New book added {request}"


@app.get("/book/{book_id}")
def get_book(book_id: int):
    try:
        return database.get_book(book_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail=repr(e))
