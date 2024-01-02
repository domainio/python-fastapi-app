
from . import schemas
from . import database


def convert_into_book_db_model(book: schemas.Book):
    return database.Book(title=book.title, number_of_pages=book.number_of_pages)


def convert_info_author_db_model(author: schemas.Author):
    return database.Author(first_name=author.first_name, last_name=author.last_name)
