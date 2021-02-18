[![Build Status](https://travis-ci.com/Njaya2019/Store.svg?branch=develop)](https://travis-ci.com/Njaya2019/Store)[![Coverage Status](https://coveralls.io/repos/github/Njaya2019/Store/badge.svg?branch=develop)](https://coveralls.io/github/Njaya2019/Store?branch=develop)
# Store
An API where an admin add products, customers adds product items to the cart and then process the order can order their desired items in the cart.

## Language
```
Python
```

## Frameworks
```
- Django
- Django rest framework
- Django allauth
```

## Openid connect provider
```
- google
```

## Views
### Add product
```
POST products/add_product 
    {
        "product_name": "the product name", 
        "product_amount": "product quantity an integer", 
        "product_price": "product quantity an integer too"
    }
```
### Add product to cart
```
POST cart/<int:product_id>/add_to_cart
    {
        "amount_to_order": "product quantity to order"
    }
```
### Make an order
```
POST orders/make_order
```
### Signup
```
POST users/signup 
    {
        "email": "your email", 
        "firstname": "your firstname", 
        "password": "your desired password", 
        "confirm_password": "the password you had provided in the previous field",
        "phone": "your valid phone number"
    }
```
### Signin
#### Signin via the API
```
POST users/signin 
    {
        "email": "your email",
        "password": "the password you had signup with"
    }
```

#### Signin via the google account
**Note** This should be done only on the **browsable API**.
After the authentication by google you'll be directed to home
view, displays a list of all products.
##### The login route by google
```
GET /accounts/google/login
```

### Issueing requests to protected API routes
#### postman clients
For postman clients after logging in they'll have to provide **X-CSRFToken** in the request header. This token is found in the
cookies section on postman in the format shown below.
```
csrftoken = 'the token on the postman cookie'
```
##### postman csrf token request header format
```
X-CSRFToken: 'the token'
```
#### Browsable API
For browsable api just login and use the API resources, you can
signin with a google account if you have one.

#### Run API in postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/86fd1f9646d733e5e1e8)

### Sms service - Africa’s Talking SMS gateway 
#### The API uses sandbox
Before making an order provide your phone number on the sandbox,
after the order is successfully made, you should see a similar message on the sandbox like the one below; 
```
order serial No. 1, customer name: Andrew
date ordered: 18-02-21 03:40:40 AM
---------------------
Pdct Qty tlt
----------------------
Iphone7 1 400
---------------------
total 400

a few seconds ago
```
## Installation
**Clone**
```
git clone git@github.com:Njaya2019/Store.git
```
**Directory**
change directory to the Store folder, the root directory of the project
```
> cd Store
```
**Install all dependencies**
```
pip install requirements.txt
```
**Set environment variable for the database.**
```
DATABASE_URL=psql://USER:PASSWORD@HOST/your-database
```
**Run migrations**
```
- python manage.py makemigrations
```
```
- python manage.py migrate
```
**run the application**
```
python manage.py runserver
```

**NOTE** When running __make order view__ make sure you have an
internet connection else you'll get an internet connection error.

## Collaborators
[Andrew Njaya](https://github.com/Njaya2019)

## References
- [Python](https://docs.python.org/3.6/)
- [Django framework](https://www.djangoproject.com/)
- [Django rest framework](https://www.django-rest-framework.org/)
