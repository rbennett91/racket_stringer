# racket_stringer
A Python and Django tennis racket stringing app

## Motivation
I string tennis rackets, both for myself and for friends and teammates. This webapp manages the rackets I string by:
* tracking customers and their orders
* maintaining a database with rackets and strings (shamelessly scraped from [Klipper USA](https://klipperusa.com/) and [Tennis Warehouse University](http://twu.tennis-warehouse.com))
* cataloging all pertinent order information in one place (strings + tension to use, string pattern of racket, due date, etc)

### Getting Started with Development

#### Clone Repository
```
git clone https://github.com/rbennett91/racket_stringer.git
```

#### System Packages
You'll need to install system-wide packages to setup a development environment. On an Ubuntu 20.04 machine:
```
sudo apt install gcc postgresql-12 libpq-dev python3-venv python3-dev
```

#### Create a Database
Inside Postgres:
```
CREATE ROLE <role_name_here> WITH LOGIN PASSWORD '<password_here>';
CREATE DATABASE <database_name_here> WITH OWNER <role_name_here>;
```

Note the role name, password, and database name.

#### Create a Virtual Environment
In the top-level of the code repository:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
```

Note that you might see miscellaneous errors like `ERROR: Failed building wheel for <package>`. These may be ignored.

#### Set Environment Variables
This project uses environment variables to manage sensitive information like the database connection and Django's `SECRET_KEY`. Create an environment variable file by copying the included template:
```
cp racket_stringer/settings/app.env.example racket_stringer/settings/app.env
```

Do not add sensitive information to the template.

Instead, open the new `racket_stringer/settings/app.env` with your favorite text editor, uncomment the block of environment variables that pertain to your shell, and fill out the missing values. Then, source the `app.env` file:

```
source racket_stringer/settings/app.env
```

Note that you'll need to re-source this file if you make changes to it. This file should be kept out of source control, and it is included in this project's `.gitignore`. Moving or renaming this file will require an update to `.gitignore` to keep it out of source control.

#### Run Django Migrations
```
python manage.py migrate
```

#### Populate the Database
Use the custom Django Management Commands to add new rackets and strings to the database:
```
python manage.py import_rackets
python manage.py import_strings
```

#### Create a User
```
python manage.py createsuperuser
```

#### Run the Development Server
```
python manage.py runserver_plus 0.0.0.0:8080
```

Visit http://<server_domain>:8080/racket_stringer in your web browser and login with the newly created user.

### Built and Deployed with
* Python 3.9.5
* PostgreSQL 13.5

### Future Ideas
Deploy as a managed app on Digital Ocean

### Guides Used in Deployment
* [Setting up Django and your web server with uWSGI and nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
* [Deploying Django applications in production with uwsgi and nginx](https://medium.com/all-about-django/deploying-django-applications-in-production-with-uwsgi-and-nginx-78aac8c0f735)
* [How To Secure Nginx with Let's Encrypt on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)

### License
MIT
