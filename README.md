# Customer Project

## About The Project:

In this project, we created a customer registration form using Django framework. This
registration form gives Name, Surname, Tc Number, City, District information from the user and saves them information to the system. Also this project allows us to update customer information and delete the registered customer. Last thing about this project, in the homepage users can see the customer list and search specific customers.

## Built with:

### Backend:
* Python
* Django
* PostgreSql
    
### Frontend:
* HTML
* CSS

## Installitation:

###### 1. Clone the repo

###### 2. Install The Requirements

    pip install requirement.txt

###### 3. Database Process

    CREATE DATABASE project_db_name

    CREATE USER projectuser WITH PASSWORD 'password';

    GRANT ALL PRIVILEGES ON DATABASE project_db_name TO projectuser

    After that define your database informations to setting.py or environ file.

###### 4. Create Database

    python manage.py makemigrations

    python manage.py migrate

###### 5. Create User For Project

    python manage.py createsuperuser 

After than you can define your username and password.

###### 6. Run Project

    python manage.py runserver

    