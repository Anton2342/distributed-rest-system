\# Distributed REST System – Products \& Stock Services



\## Opis projektu



Projekt przedstawia prosty system rozproszony składający się z dwóch niezależnych mikroserwisów komunikujących się poprzez REST API.



System składa się z:



---



\## 🟦 1. Products Service (Serwis Produktów)

\- Port: \*\*8001\*\*

\- Endpoint: `GET /products/{id}`

\- Serwis przechowuje dane produktów w pamięci i zwraca je w formacie JSON.

\- W przypadku nieistniejącego produktu zwraca \*\*HTTP 404\*\*.



Przykładowa odpowiedź:

```json

{

&nbsp; "id": 1,

&nbsp; "name": "Laptop",

&nbsp; "price": 4500.0

}



