import { useEffect, useState } from "react";

/*
  PRODUCT FORM
  ------------
  Used for both Add and Update.
  If editingProduct is set, the form switches to "Update" mode.
*/

const EMPTY_FORM = {
  name: "",
  description: "",
  price: "",
  quantity: "",
};

function ProductForm({ editingProduct, onSubmit, onCancel }) {
  const [form, setForm] = useState(EMPTY_FORM);

  useEffect(() => {
    if (editingProduct) {
      setForm({
        name: editingProduct.name,
        description: editingProduct.description || "",
        price: editingProduct.price,
        quantity: editingProduct.quantity,
      });
    } else {
      setForm(EMPTY_FORM);
    }
  }, [editingProduct]);

  function handleChange(event) {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  function handleSubmit(event) {
    event.preventDefault();
    onSubmit({
      name: form.name.trim(),
      description: form.description.trim(),
      price: Number(form.price),
      quantity: Number(form.quantity),
    });

    if (!editingProduct) {
      setForm(EMPTY_FORM);
    }
  }

  const isEdit = Boolean(editingProduct);

  return (
    <form className="product-form" onSubmit={handleSubmit}>
      <h2>{isEdit ? "Update product" : "Add a product"}</h2>

      <label>
        Name
        <input
          name="name"
          value={form.name}
          onChange={handleChange}
          placeholder="Wireless Mouse"
          required
        />
      </label>

      <label>
        Description
        <textarea
          name="description"
          value={form.description}
          onChange={handleChange}
          placeholder="Short details about the product"
          rows="3"
        />
      </label>

      <div className="form-row">
        <label>
          Price
          <input
            name="price"
            type="number"
            min="0.01"
            step="0.01"
            value={form.price}
            onChange={handleChange}
            placeholder="799"
            required
          />
        </label>

        <label>
          Quantity
          <input
            name="quantity"
            type="number"
            min="0"
            step="1"
            value={form.quantity}
            onChange={handleChange}
            placeholder="10"
            required
          />
        </label>
      </div>

      <div className="form-actions">
        <button type="submit" className="btn primary">
          {isEdit ? "Save changes" : "Add product"}
        </button>
        {isEdit && (
          <button type="button" className="btn ghost" onClick={onCancel}>
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}

export default ProductForm;
