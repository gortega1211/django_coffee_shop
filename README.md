# Django Coffee Shop Project

## Description

Simple project with multiple elemental features in Django and Django Rest Framework.

## Requirements 📋

- Python v3.12.2
- PostgreSQL v16
- Libraries inside of [requirements](requirements.txt)
- Optionally, you can install the libraries inside of [requirements-dev](requirements-dev.txt) to develop.

## Installation Guide

Follow these steps to get the project up and running on your local machine.

### 1\. Clone the Repository

Clone the project repository from GitHub to your local machine.

```bash
git clone https://github.com/gortega1211/django_coffee_shop.git coffee_shop
cd coffee_shop
```

### 2\. Set Up Virtual Environment

Create and activate a virtual environment.

```bash
python3 -m venv venv 
source venv/bin/activate 
```

### 3\. Install Dependencies

Install the required Python packages using `pip`.

`pip install -r requirements.txt`

### 4\. Configure Environment Variables

Create a `.env` file in the root of the project. You can use `.env.example` as a template.

`cp .env.example .env`

Update the `.env` file with your database credentials and other necessary configurations.

### 5\. Set Up the Database

Create the PostgreSQL database (review [db_managment](db_managment.sql)) and apply migrations.

```bash
psql -U postgres CREATE DATABASE coffeeshop;
```
Apply migrations 

```bash
python manage.py migrate
```

### 6\. Create a Superuser

Create a superuser to access the Django admin interface.

```
python manage.py createsuperuser
```

### 7\. Run the Development Server

Start the Django development server.

```
python manage.py runserver
```

### 8\. Provide Initial Data (Optional)

Load the Product fixture.

```
python manage.py loaddata products_data
```

Access the project by navigating to `http://127.0.0.1:8000` in your web browser.

Project Structure
-----------------

*   **products**: Handles everything related to coffee products.
*   **users**: Manages user authentication and profiles.
*   **orders**: Manages customer orders.

## Author ✒️

- **Gustavo Ortega Palacios** - [gortega1211](https://https://github.com/gortega1211)