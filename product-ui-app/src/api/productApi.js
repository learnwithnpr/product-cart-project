/*
  API LAYER
  ---------
  All HTTP calls to FastAPI live here.

  Teaching point:
    Components should not call fetch() everywhere.
    Keep network code in one place (like a backend service).
*/

const API_BASE = "http://localhost:8000/products";

async function handleResponse(response) {
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    const message =
      typeof error.detail === "string" ? error.detail : "API request failed";
    throw new Error(message);
  }
  return response.json();
}

export async function getProducts() {
  const response = await fetch(API_BASE);
  return handleResponse(response);
}

export async function createProduct(product) {
  const response = await fetch(API_BASE, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(product),
  });
  return handleResponse(response);
}

export async function updateProduct(id, product) {
  const response = await fetch(`${API_BASE}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(product),
  });
  return handleResponse(response);
}

export async function deleteProduct(id) {
  const response = await fetch(`${API_BASE}/${id}`, {
    method: "DELETE",
  });
  return handleResponse(response);
}
