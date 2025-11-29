# Distributed REST System — Products & Stock Services



Projekt przedstawia prosty system rozproszony składający się z dwóch mikroserwisów komunikujących się poprzez REST API
System demonstruje komunikację między dwoma niezależnymi usługami REST.

---

## Struktura repozytorium

distributed-rest-system/
│
├── products_service/
│   └── main.py
│
├── stock_service/
│   └── main.py
│
└── README.md

---

## Jak uruchomić serwisy

###  1. Products Service (port 8001)

cd products_service
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --host 127.0.0.1 --port 8001 --reload

### ▶️ 2. Stock Service (port 8002)

cd stock_service
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn httpx
uvicorn main:app --host 127.0.0.1 --port 8002 --reload








