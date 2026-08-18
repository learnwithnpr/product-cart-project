import { useEffect, useState } from "react";
import ProductForm from "./components/ProductForm.jsx";
import ProductList from "./components/ProductList.jsx";
import {
  getProducts,
  createProduct,
  updateProduct,
  deleteProduct,
} from "./api/productApi.js";

function App() {
  const [products, setProducts] = useState([]);
  const [editingProduct, setEditingProduct] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  async function loadProducts() {
    try {
      setError("");
      const data = await getProducts();
      setProducts(data);
    } catch (err) {
      setError(
        "Cannot load products. Is the FastAPI backend running on port 8000?"
      );
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadProducts();
  }, []);

  async function handleSave(formData) {
    try {
      setError("");
      if (editingProduct) {
        await updateProduct(editingProduct.id, formData);
        setEditingProduct(null);
      } else {
        await createProduct(formData);
      }
      await loadProducts();
    } catch (err) {
      setError(err.message);
    }
  }

  async function handleDelete(id) {
    const confirmed = window.confirm("Delete this product?");
    if (!confirmed) {
      return;
    }

    try {
      setError("");
      await deleteProduct(id);
      if (editingProduct?.id === id) {
        setEditingProduct(null);
      }
      await loadProducts();
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="page">
      <header className="hero">
        <p className="eyebrow">Student demo</p>
        <h1>Product Card Manager</h1>
        <p>Add, view, update, and delete products stored in PostgreSQL.</p>
      </header>

      {error && <div className="banner error">{error}</div>}

      <div className="layout">
        <ProductForm
          editingProduct={editingProduct}
          onSubmit={handleSave}
          onCancel={() => setEditingProduct(null)}
        />

        <div>
          <div className="list-header">
            <h2>Products</h2>
            <button className="btn ghost" onClick={loadProducts}>
              Refresh
            </button>
          </div>
          {loading ? (
            <p className="empty-state">Loading products...</p>
          ) : (
            <ProductList
              products={products}
              onEdit={setEditingProduct}
              onDelete={handleDelete}
            />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
