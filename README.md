# Triduum_test

## Table of Contents
- [Triduum\_test](#triduum_test)
  - [Table of Contents](#table-of-contents)
  - [General Info](#general-info)
  - [Technologies](#technologies)
  - [Installation](#installation)
***

## General Info
Ecommerce API built in Django rest framework using Python.  Project was developed by Kevin Andres Blandon Velez for Triduum.

## Technologies
***
A list of technologies used within the project:
* [Django](https://www.djangoproject.com/): Version 4.1.7
* [Djangorestframework](https://www.django-rest-framework.org/): Version 3.14.0
* [Python](https://www.python.org/): Version 3.11

## Installation
***
About the installation:

Use pip
You can install the project by running this command:
```
py -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
py .\manage.py makemigrations
py .\manage.py migrate
py .\manage.py runserver
```