# Django Customer Relationship Management

![image](https://user-images.githubusercontent.com/71379045/168422458-98dbd26d-f6be-4db5-b9ae-fb1d3279592c.png)

This is my first Django project, so i'll write a guide with some important steps and commands for Django development

## Virtual Environments

- Good to run the application in an isolated environment
- Create and manage separete environments for each Python project on the same computer
- use venv module (one option) on the root of yout project

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To leave the virtual environment type deactivate

```bash
(.venv) % deactivate
```

## Install Django

Inside the virtual environment type

```bash
(.venv) > python -m pip install django
```

## Start Django Project

```bash
(.venv) > django-admin startproject CRM .
```

## Run Django Project

The bellow command will run the Django's internal web server, this is suitable for local development purposes

```bash
(.venv) % python3 manage.py runserver
```

## Create an App

Each Django project has many apps and each app should have a pourpose like autenticate users and handle payments

```bash
(.venv) % python3 manage.py startapp accounts
```

## Migrate and Run Migrations

```bash
(.venv) > python manage.py migrate
```

## Class-Based Views vs Function-Based Views

https://docs.djangoproject.com/en/4.0/topics/class-based-views/intro/
