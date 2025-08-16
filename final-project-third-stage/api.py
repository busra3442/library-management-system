from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library, Book  # Senin Aşama 1'de yazdığın sınıflar
import httpx
from typing import List

app = FastAPI()
library = Library("library.json")

# Request modeli
class ISBNRequest(BaseModel):
    isbn: str

# Response modeli
class BookResponse(BaseModel):
    title: str
    authors: List[str]  # 'authors' listesi
    isbn: str


@app.get("/books", response_model=list[BookResponse])
def get_books():
    books = library.list_books()
    return [
        {
            "title": b.title,
            "authors": [b.authors] if isinstance(b.authors, str) else b.authors,  # tek string’i listeye al
            "isbn": b.isbn
        }
        for b in books
    ]



@app.post("/books", response_model=BookResponse)
def add_book(isbn_request: ISBNRequest):
    isbn = isbn_request.isbn

    # Library ISBN’den kitabı eklesin
    library.add_book(isbn)

    # Eklenen kitabı bul
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")

    return {
        "title": book.title,
        "authors": book.authors.split(", ") if isinstance(book.authors, str) else book.authors,
        "isbn": book.isbn
    }




@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    try:
        library.remove_book(isbn)
        return {"message": "Kitap silindi"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
