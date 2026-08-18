# Product Backend Service

FastAPI + PostgreSQL for Product CRUD.

Used by `product-ui-app`.

## Folders

```
product-backend-service/
├── requirements.txt     # Python libraries
├── .env.example         # Database username/password
└── app/
    ├── main.py          # Starts the app
    ├── config.py        # Reads .env
    ├── database.py      # Postgres connection
    ├── models/          # Database table
    ├── schemas/         # JSON request/response
    ├── services/        # Create / Read / Update / Delete
    └── controllers/     # HTTP URLs
```

Simple flow:

```
React UI -> Controller -> Service -> Model -> PostgreSQL
```

## APIs

| Method | URL | What it does |
|--------|-----|----------------|
| GET | `/products` | Show all products |
| GET | `/products/{id}` | Show one product |
| POST | `/products` | Add a product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |

## Steps to run

1. PostgreSQL should be running.

2. Create the database:

```sql
CREATE DATABASE product_db;
```

3. Install Python libraries:

```bash
cd product-backend-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

4. Create `.env` and put your Postgres username and password:

```bash
cp .env.example .env
```

Windows:

```bash
copy .env.example .env
```

Example `.env`:

```
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/product_db
```

5. Start the API:

```bash
uvicorn app.main:app --reload
```

- http://localhost:8000
- http://localhost:8000/docs

## Sample JSON for POST /products

```json
{
  "name": "Wireless Mouse",
  "description": "Comfortable USB mouse",
  "price": 799,
  "quantity": 25
}
```
