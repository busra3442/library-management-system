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
library-app/
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


## 🖥️ Örnek Çıktı 
<img width="360" height="577" alt="ekran-1" src="https://github.com/user-attachments/assets/ecd96702-99a9-47d1-9f6a-48c01fc69a3e" /> 
<hr/>
<img width="364" height="428" alt="ekran-3" src="https://github.com/user-attachments/assets/19fb2637-c320-4ef2-8566-2d470375d139" /> 
<hr/>
<img width="368" height="571" alt="ekran-2" src="https://github.com/user-attachments/assets/30193cea-2681-4b7f-997f-9f92f015f585" />
