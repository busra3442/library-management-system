# 📚 Python 202 Bootcamp - Aşama 1: OOP ile Terminalde Çalışan Kütüphane

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilen kütüphane uygulamasının **ilk aşamasıdır**.  
Amaç, Nesne Yönelimli Programlama (OOP) prensiplerini kullanarak terminalde çalışan bir kütüphane uygulaması geliştirmektir.  

---

## 🚀 Özellikler
- Yeni kitap ekleme  
- Kitap silme  
- Kütüphanedeki tüm kitapları listeleme  
- Eklenmiş kitaplar üzerinden ISBN ile kitap arama  
- Verilerin kalıcı olarak **JSON dosyasında (library.json)** saklanması  

---
## 🛠 Kullanılan Teknolojiler

- **Python 3.9+** → Ana programlama dili  
- **JSON** → Kitap verilerinin saklanması  
- **Pytest** → Test senaryoları 

> Aşama 1 için harici bir kütüphane kullanılmamaktadır.  
> (Aşama 2’de `httpx`, Aşama 3’te `fastapi` ve `uvicorn` eklenecektir.)

## 📂 Proje Yapısı

```bash
final-project-first-stage/
│
├── book.py             # Book sınıfı (kitap nesnesi tanımı)
├── library.py          # Library sınıfı (kütüphane yönetimi)
├── main.py             # Terminal uygulaması (menü tabanlı giriş noktası)
├── library.json        # Gerçek kütüphane verilerinin saklandığı JSON dosyası
├── test_library.json   # Testler için kullanılan sahte kütüphane dosyası
├── tests.py            # Pytest testleri (Book ve Library metodları için)
├── requirements.txt    # Bağımlılık listesi (Aşama 1’de boş kalabilir)

```
---
## ⚙️ Projenin 1.Aşamasının Kurulumu ve Çalıştırılması
- git clone https://github.com/busra3442/library-management-system.git
- cd library-management-system/final-project-first-stage  # 1. aşama klasörüne girilir
- Bağımlılıklar yüklenir (Aşama 1 için gerek yok ama requirements.txt varsa çalıştırılmalı): pip install -r requirements.txt
- python main.py # terminalde uygulama başlatılır
- pytest tests.py # testlerin çalıştırılması 

---
## 🖥️ Örnek Çıktı 
<img width="360" height="577" alt="ekran-1" src="https://github.com/user-attachments/assets/ecd96702-99a9-47d1-9f6a-48c01fc69a3e" /> 
<hr/>
<img width="364" height="428" alt="ekran-3" src="https://github.com/user-attachments/assets/19fb2637-c320-4ef2-8566-2d470375d139" /> 
<hr/>
<img width="368" height="571" alt="ekran-2" src="https://github.com/user-attachments/assets/30193cea-2681-4b7f-997f-9f92f015f585" />

# 📚 Python 202 Bootcamp - Aşama 2: Harici API ile Veri Zenginleştirme

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilen kütüphane uygulamasının **ikinci aşamasıdır**.  
Amaç, mevcut terminal uygulamasını bir **harici API (OpenLibrary)** ile entegre ederek kitap bilgilerini otomatik olarak zenginleştirmektir.  

Aşama 1’de kullanıcı kitap eklerken **başlık, yazar ve ISBN** bilgilerini manuel giriyordu.  
Aşama 2’de kullanıcı **sadece ISBN numarasını** girecek, kitap bilgileri **OpenLibrary API**’den çekilecektir.  

---

## 🚀 Özellikler
- ISBN ile kitap ekleme (OpenLibrary API’den başlık ve yazar bilgilerini çekme)  
- Kitap silme  
- Kütüphanedeki tüm kitapları listeleme  
- ISBN ile kitap arama  
- Verilerin **JSON dosyasında (library.json)** saklanması  
- Hata yönetimi (geçersiz ISBN veya internet bağlantısı yoksa kullanıcı bilgilendirilir)  

---

## 📂 Proje Yapısı

```bash
final-project-second-stage/
├── book.py             # Book sınıfı (kitap nesnesi tanımı)
├── library.py          # Library sınıfı (kütüphane yönetimi + OpenLibrary API entegrasyonu)
├── main.py             # Terminal uygulaması (ISBN ile kitap ekleme)
├── library.json        # Gerçek kütüphane verilerinin saklandığı JSON dosyası
├── test.json           # Testler için kullanılan örnek JSON dosyası
├── test_library.json   # Testler için kullanılan sahte kütüphane dosyası
├── test_library.py     # Library sınıfı için testler
├── test-isbn.py        # ISBN üzerinden API’den kitap çekme testleri
├── tests.py            # Genel pytest testleri
├── requirements.txt    # Bağımlılık listesi (httpx eklenmiştir)
```
---
## 🛠 Kullanılan Teknolojiler

- Python 3.9+ → Ana programlama dili

- httpx → OpenLibrary API’den veri çekmek için

- JSON → Kitap verilerini saklamak için

- Pytest → Test senaryoları

---
## ⚙️ Projenin 2.Aşamasının Kurulumu ve Çalıştırılması
- git clone https://github.com/busra3442/library-management-system.git
- cd library-management-system/final-project-second-stage
- pip install -r requirements.txt # Bu aşamada httpx kütüphanesi gereklidir requirements.txt dosyasında listelenmiştir
- python main.py
- pytest
---
✍️ **Not:** Aşama 2’de kitap ekleme işlemi artık ISBN tabanlı API entegrasyonu ile yapılmaktadır.  
Aşama 1’in tüm işlevleri aynı şekilde çalışmaya devam eder.

# 📚 Python 202 Bootcamp - Aşama 3: FastAPI ile Kendi API’nizi Oluşturma

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilen kütüphane uygulamasının **üçüncü aşamasıdır**.  
Amaç, terminalde çalışan uygulamanın mantığını bir **web servisi (API)** haline getirerek kitap verilerine HTTP istekleri üzerinden erişim sağlamaktır.  

---

## 🚀 Özellikler
- **GET /books** → Kütüphanedeki tüm kitapların listesini JSON olarak döndürür  
- **POST /books** → ISBN alır, OpenLibrary API’den bilgileri çeker ve kitabı ekler  
- **DELETE /books/{isbn}** → ISBN’e göre kitabı kütüphaneden siler  
- **FastAPI** sayesinde otomatik dokümantasyon `/docs` altında erişilebilir  

---

## 📂 Proje Yapısı

```bash
final-project-third-stage/
├── api.py              # FastAPI uygulaması
├── book.py             # Book sınıfı
├── library.py          # Library sınıfı (kitap yönetimi + API entegrasyonu)
├── main.py             # Terminal uygulaması (önceki aşamalardan)
├── library.json        # Kitap verilerinin saklandığı dosya
├── requirements.txt    # Bağımlılıklar (fastapi, uvicorn, httpx)
├── test_api.py         # API endpoint testleri
├── test-isbn.py        # ISBN testleri
├── test_library.py     # Library sınıfı testleri
├── tests.py            # Genel testler
├── test.json           # Test için örnek JSON
└── test_library.json   # Test için sahte JSON
```
---

## 🛠 Kullanılan Teknolojiler
- Python 3.9+ → Ana programlama dili

- FastAPI → Web API geliştirme

- Uvicorn → FastAPI sunucusu çalıştırma

- httpx → OpenLibrary API çağrıları

- Pydantic → Veri modelleri

- JSON → Kitap verilerini saklama

- Pytest → Test senaryoları
---

## ⚙️ Projenin 2.Aşamasının Kurulumu ve Çalıştırılması
- git clone https://github.com/busra3442/library-management-system.git
- cd library-management-system/final-project-third-stage
- pip install -r requirements.txt
- uvicorn api:app --reload # api sunucusunu başlatır
- Sunucu çalıştığında şu adrese gidin:
👉 http://127.0.0.1:8000/docs
Buradan tüm endpoint’leri interaktif olarak test edebilirsiniz.
- pytest test_api.py
---
✍️ Not: Bu aşamada, Aşama 1 ve 2’nin tüm işlevleri korunur.
Ekstra olarak, uygulamamız artık web tabanlı bir API üzerinden kullanılabilir hale gelir.





