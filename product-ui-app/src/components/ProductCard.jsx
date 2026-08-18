/*
  PRODUCT CARD
  ------------
  Shows one product. Edit and Delete buttons call parent handlers.
*/

function ProductCard({ product, onEdit, onDelete }) {
  return (
    <article className="product-card">
      <div className="card-top">
        <h3>{product.name}</h3>
        <span className="price">₹{Number(product.price).toFixed(2)}</span>
      </div>

      <p className="description">
        {product.description || "No description provided."}
      </p>

      <p className="quantity">
        In stock: <strong>{product.quantity}</strong>
      </p>

      <div className="card-actions">
        <button className="btn" onClick={() => onEdit(product)}>
          Edit
        </button>
        <button className="btn danger" onClick={() => onDelete(product.id)}>
          Delete
        </button>
      </div>
    </article>
  );
}

export default ProductCard;
