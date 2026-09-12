# B2B Request for Quotation (RFQ) Marketplace

A full-stack B2B Request for Quotation (RFQ) Marketplace that allows buyers to create and manage requests for quotations and suppliers to submit quotations for those requests.

The application provides role-based access for Buyers and Suppliers, REST APIs using Django REST Framework, authentication, RFQ and quotation management, and a responsive frontend built with HTML, CSS, and JavaScript.

## Live Application

**Live URL:**  
https://rfq-marketplace-ejob.onrender.com

## GitHub Repository

**Repository:**  
https://github.com/maheshkunchala0717-sudo/Request_for_Quotations_project

---

## Features

### Authentication

- User registration
- User login
- Token/JWT-based authentication
- Buyer and Supplier roles
- Role-based access control

### Buyer Features

- Create RFQs
- View RFQs
- View individual RFQ details
- Edit RFQs
- Delete RFQs
- View supplier quotations
- Select a quotation

### Supplier Features

- View available RFQs
- View RFQ details
- Submit quotations
- View submitted quotations
- Edit quotations
- Delete quotations

### RFQ Management

Each RFQ can contain:

- Product/Service
- Description
- Quantity
- Delivery location
- Deadline
- Buyer information

### Quotation Management

Each quotation can contain:

- Price
- Delivery time
- Additional notes
- Supplier information
- Associated RFQ

### Other Features

- Django Admin interface
- RESTful API endpoints
- PostgreSQL database in production
- SQLite database for local development
- Static file handling with WhiteNoise
- CORS configuration
- Responsive frontend
- CRUD operations for RFQs and quotations

---

## Technology Stack

### Backend

- Python
- Django
- Django REST Framework
- Django REST Framework Token Authentication
- Simple JWT
- Django Filters

### Frontend

- HTML5
- CSS3
- JavaScript

### Database

- PostgreSQL - Production
- SQLite - Local development

### Deployment

- Render Web Service
- Render PostgreSQL

### Development Tools

- Git
- GitHub
- VS Code

---

## Project Architecture

The application follows a simple full-stack architecture.

```text
User
  |
  v
Frontend
HTML / CSS / JavaScript
  |
  | HTTP Requests
  v
Django REST Framework APIs
  |
  +-------------------+
  |                   |
  v                   v
Authentication     Business Logic
  |                   |
  +---------+---------+
            |
            v
        Database
            |
     +------+------+
     |             |
   SQLite       PostgreSQL
   (Local)      (Production)
