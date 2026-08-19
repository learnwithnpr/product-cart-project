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

## Install Node.js first (required)

`npm` comes with Node.js. If `node -v` or `npm -v` fails, install Node.js **LTS**.

1. Open https://nodejs.org
2. Click the **LTS** button (recommended)
3. Download the installer for your system
4. Run the installer (keep the npm checkbox enabled)
5. **Close the terminal and open a new one**
6. Check:

```bash
node -v
npm -v
```

Both should print a version (Node 18 or 20 is fine).

**Windows:** download the `.msi` installer  
**macOS:** download the `.pkg` installer  
**Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install -y nodejs npm
node -v
npm -v
```

If Git is also missing (`git --version` fails), install Git from https://git-scm.com or use **Code → Download ZIP** on GitHub.

## Steps to run

Start the backend first: http://localhost:8000

Then:

```bash
git clone https://github.com/learnwithnpr/product-cart-project.git
cd product-cart-project/product-ui-app
npm install
npm run dev
```

Open http://localhost:5173
