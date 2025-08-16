from library import Library

def main():
    library = Library()

    while True:
        print("\n--- Kütüphane Uygulaması ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            isbn = input("ISBN girin: ")
            library.add_book(isbn)

        elif choice == "2":
            isbn = input("Silmek istediğiniz kitabın ISBN numarası: ")
            library.remove_book(isbn)

        elif choice == "3":
            books = library.list_books()
            if not books:
                print("Kütüphanede kitap yok.")

        elif choice == "4":
            isbn = input("Aranan kitabın ISBN numarası: ")
            book = library.find_book(isbn)
            if book:
                print(f"{book.title} - {book.authors} (ISBN: {book.isbn})")
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
