# E-Commerce API

This is a Django REST Framework-based API for an E-Commerce application. It includes user authentication, product management, and order processing.

## Features
- **User Management**
  - User registration with token-based authentication.
  - Secure password storage and retrieval.

- **Product Management**
  - List and filter products by category, price, and stock availability.
  - Pagination for large datasets.
  - Authenticated users can create products.
  - Only the owner can update or delete their products.

- **Order Management**
  - Authenticated users can create orders.
  - Stock quantity automatically updates when an order is created.
  - Users can view their orders.
  - Only the owner of an order can delete it.