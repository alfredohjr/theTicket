# theTicket

This is a simple ticketing system that allows users to create, view, and delete tickets. 

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)

## Installation

Clone the repository using the following command:

```bash
git clone https://github.com/alfredohjr/theTicket.git
```

Create a virtual environment.

```bash
python3 -m venv venv
```

Intall dependencies.

```bash
pip install -r requirements.txt
```

Migrate and create the database.

```bash
python manage.py migrate
```

Create the superuser.

```bash
python manage.py createsuperuser
```

Run the server.

```bash
python manage.py runserver
```

To run the tests, use the following command:

```bash
python manage.py test
```

## Usage

To use the application, navigate to the following URL: http://localhost:8000/admin/ and login with the superuser credentials. Once logged in, you can create, view, and delete tickets.

See Swagger Documentation in following URL: http://localhost:8000/swagger/

