# Portfolio (Backend part)

This is the backend part of web application Portfolio which is based on Django Rest Framework (Python)

Frontend part: [portfolio-fe (Github)](https://github.com/stepan323446/portfolio-fe)

## Project Overview

Portfolio-be provides an API for managing personal information. Users can easily add their projects and update their biography, which will later be displayed on the frontend.

## Features
- Built with **Django REST Framework** for creating RESTful API endpoints
- Integrated **DRF Spectacular** for automatic OpenAPI schema and Swagger documentation generation
- Uses **Django CKEditor** for rich text content editing

## Installing

### Manually

Look at the [Django documentation](https://docs.djangoproject.com/en/6.0/topics/install/) to learn more.

1. Create environment and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Create a `.env` file and based on `.env.example`.

3. Install MySQL and create a new database. Then apply migrations:
```
python3 manage.py migrate
```

4. Collect static files (required for the Django admin panel):
```
python3 manage.py collectstatic
```

5. Run the development server:
```
python3 manage.py runserver
```