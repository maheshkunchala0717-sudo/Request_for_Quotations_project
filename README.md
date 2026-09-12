# B2B Request for Quotation (RFQ) Marketplace

A full-stack B2B RFQ Marketplace where Buyers can create and manage RFQs and Suppliers can submit quotations.

## Live Application

https://rfq-marketplace-ejob.onrender.com

## GitHub Repository

https://github.com/maheshkunchala0717-sudo/Request_for_Quotations_project

## Features

- Buyer and Supplier registration/login
- Role-based authentication and permissions
- Create, view, update and delete RFQs
- Create, view, update and delete quotations
- Select supplier quotations
- Django Admin
- REST APIs
- Responsive frontend

## Technology Stack

- **Backend:** Python, Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (local), PostgreSQL (production)
- **Deployment:** Render
- **Authentication:** Token Authentication / JWT

## Architecture

```text
Frontend (HTML/CSS/JavaScript)
            |
            v
Django REST Framework
            |
            v
     Database
   SQLite / PostgreSQL

Project Structure

rfq_marketplace/
├── accounts/
├── frontend/
├── market/
├── manage.py
└── requirements.txt

Local Setup

git clone https://github.com/maheshkunchala0717-sudo/Request_for_Quotations_project.git
cd Request_for_Quotations_project/rfq_marketplace/market
python -m venv marketplace
marketplace\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Open: http://127.0.0.1:8000/

API Endpoints

POST /register/
POST /login/

GET/POST /rfqs/
GET/PUT/DELETE /rfqs/<id>/

GET/POST /quatations/
GET/PUT/DELETE /quatations/<id>/

Assumptions & Limitations
Buyers create RFQs and Suppliers submit quotations.
Authentication is required for protected operations.
Email notifications and payment processing are not included.
The application is deployed on a free hosting plan.
Author

Mahesh Kunchala

GitHub:
https://github.com/maheshkunchala0717-sudo
