[![Build Status](https://travis-ci.com/Njaya2019/Store.svg?branch=ch-update-readme)](https://travis-ci.com/Njaya2019/Store)[![Coverage Status](https://coveralls.io/repos/github/Njaya2019/Store/badge.svg?branch=develop)](https://coveralls.io/github/Njaya2019/Store?branch=develop)
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
```
## Views
### Add product
```
POST products/add_product {"product_name": "the product name", "product_amount": "product quantity an integer", "product_price": "product quantity an integer too"}
```
### Add product to cart
```
POST cart/<int:product_id>/add_to_cart {"amount_to_order": "product quantity to order"}
```
### Make an order
```
POST orders/make_order
```
### Signup
```
POST users/signup {"email": "your email", "firstname": "your firstname", "password": "your desired password", "confirm_password": "the password you had provided in the previous field"}
```
### Signin
```
POST users/signin {"email": "your email", "password": "the password you had signup with"}
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
DATABASE_URL=psql://USER:PASSWORD@HOST:HOST/your-database
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
## Collaborators
[Andrew Njaya](https://github.com/Njaya2019)

## References
- [Python](https://docs.python.org/3.6/)
- [Django framework](https://www.djangoproject.com/)
- [Django rest framework](https://www.django-rest-framework.org/)
