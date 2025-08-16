import httpx

isbn = "9780140328721"
url = f"https://openlibrary.org/isbn/{isbn}.json"
resp = httpx.get(url, timeout=10.0)
print(resp.status_code)
print(resp.text[:200])  # ilk 200 karakterini göster
