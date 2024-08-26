# Flipr_Backend-task
This project is a Django REST API that implements JWT authentication and basic CRUD operations for managing products. It includes endpoints for user authentication, product creation, listing, updating, and deletion.
Features

    JWT Authentication: Secure user authentication using JWT (JSON Web Token).
    CRUD Operations: Create, Read, Update, and Delete products.
    Postman Documentation: Use Postman for easy API testing and exploration.
    Django REST Framework: For creating APIs with ease and structure.

Technologies Used

    Django: Backend framework.
    Django REST Framework (DRF): To build APIs.
    djangorestframework-simplejwt: JWT authentication for securing endpoints.
    SQLite: Default database.
    Postman: API testing and documentation.

Installation
Prerequisites

    Python 3.x
    Django 4.x
    Postman (for testing, optional)
    
Setup Instructions

Install Dependencies

    pip install -r requirements.txt

Run Migrations

    python manage.py migrate

Create a Superuser

     python manage.py createsuperuser

Run the Server

    python manage.py runserver

The server will run on http://127.0.0.1:8000/.

Usage
Authentication
    Sign Up:
        Create a user by accessing the Django admin at http://127.0.0.1:8000/admin/ (use your superuser credentials).
    Sign In:
        Send a POST request to /auth/signin/ with your username and password to receive a JWT token.Usage
json

    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    You will receive the access and refresh tokens in the response.

Products API

    Authorization: All requests to product-related endpoints need to include the Authorization: Bearer <access_token> header.
    CRUD Operations:
        Create a Product: Send a POST request to /products/.
        List Products: Send a GET request to /products/.
        Update a Product: Send a PUT or PATCH request to /products/<id>/.
        Delete a Product: Send a DELETE request to /products/<id>/.
        
Testing with Postman

To test the API using Postman:

    Import the provided Postman collection or create your own.
    Set up the requests with the appropriate endpoints and methods.
    Add the JWT token in the Authorization header for protected routes.
    
API Endpoints

    Method	 Endpoint	        Description               	Auth Required
    POST	  /auth/signin/	    Obtain JWT token                No
    GET	    /products/	      Get all products	              Yes
    POST	  /products/	      Create a new product	          Yes
    GET   	/products/<id>/   Get details of a product	      Yes
    PUT   	/products/<id>/   Update an existing product	    Yes
    DELETE	/products/<id>/	  Delete a product	              Yes
