# Product UI App

React UI for Product Card management.

Talks to `product-backend-service`.

## Folders

```
product-ui-app/
├── package.json
├── index.html
└── src/
    ├── main.jsx              # Starts React
    ├── App.jsx               # Main screen
    ├── api/productApi.js     # Calls FastAPI
    └── components/
        ├── ProductForm.jsx   # Add / Update
        ├── ProductList.jsx   # All cards
        └── ProductCard.jsx   # One card
```

## Features

1. Add a product
2. Show product cards
3. Update a product
4. Delete a product

## Steps to run

Start the backend first: http://localhost:8000

Then:

```bash
cd product-ui-app
npm install
npm run dev
```

Open http://localhost:5173
