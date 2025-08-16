import json
import httpx
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()  # Dosyadan sadece bir kez yükle

    def add_book(self, isbn):
        # Eğer kitap zaten varsa ekleme
        if self.find_book(isbn):
            print("Bu kitap zaten kütüphanede mevcut.")
            return

        url = f"https://openlibrary.org/isbn/{isbn}.json"

        try:
            response = httpx.get(url, timeout=10.0, follow_redirects=True)
            response.raise_for_status()
        except httpx.HTTPStatusError:
            print("Kitap bulunamadı.")
            return
        except Exception as e:
            print(f"Hata: {e}")
            return

        data = response.json()
        title = data.get("title", "Bilinmiyor")

        authors = []
        for author in data.get("authors", []):
            author_key = author.get("key")
            if author_key:
                author_url = f"https://openlibrary.org{author_key}.json"
                try:
                    author_resp = httpx.get(author_url, timeout=10.0, follow_redirects=True)
                    author_resp.raise_for_status()
                    author_data = author_resp.json()
                    authors.append(author_data.get("name", "Bilinmiyor"))
                except:
                    authors.append("Bilinmiyor")
            else:
                authors.append("Bilinmiyor")

        new_book = Book(
            title=title,
            authors=", ".join(authors) if authors else "Bilinmiyor",
            isbn=isbn
        )

        self.books.append(new_book)
        self.save_books()
        print(f"Kitap eklendi: {new_book}")

    def remove_book(self, isbn: str):
        book = self.find_book(isbn)
        if not book:
            print("Kitap bulunamadı.")
            return
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()
        print(f"{isbn} numaralı kitap silindi.")

    def list_books(self):
        if not self.books:
            print("Kütüphane boş.")
            return []
        for book in self.books:
            print(f"{book.title} - {book.authors} (ISBN: {book.isbn})")
        return self.books

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                books_data = json.load(f)
                seen_isbns = set()
                self.books = []
                for book_dict in books_data:
                    if book_dict['isbn'] not in seen_isbns:
                        self.books.append(Book(**book_dict))
                        seen_isbns.add(book_dict['isbn'])
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)
