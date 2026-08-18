import ProductCard from "./ProductCard.jsx";

/*
  PRODUCT LIST
  ------------
  Renders a card for every product.
*/

function ProductList({ products, onEdit, onDelete }) {
  if (products.length === 0) {
    return (
      <div className="empty-state">
        No products yet. Add your first product using the form.
      </div>
    );
  }

  return (
    <section className="product-grid">
      {products.map((product) => (
        <ProductCard
          key={product.id}
          product={product}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </section>
  );
}

export default ProductList;
