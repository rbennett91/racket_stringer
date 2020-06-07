# racket_stringer
A Python and Django tennis racket stringing CMS

## How Does it Work?
...

## Getting Started with Development

### Clone Repository
```
git clone https://github.com/rbennett91/racket_stringer.git
```

### System Packages
You'll need to install system-wide packages to setup a development environment. On an Ubuntu 20.04 machine:
```
sudo apt install gcc postgresql-12 libpq-dev python3-venv python3-dev
```

### Create a Database
Inside Postgres:
```
CREATE ROLE <role_name_here> WITH LOGIN PASSWORD '<password_here>';
CREATE DATABASE <database_name_here> WITH OWNER <role_name_here>;
```

Note the role name, password, and database name.

### Create a Virtual Environment
In the top-level of the code repository:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
```

Note that you might see miscellaneous errors like `ERROR: Failed building wheel for <package>`. These may be ignored.

### Set Environment Variables
This project uses environment variables to manage sensitive information like the database connection and Django's `SECRET_KEY`. Create an environment variable file by copying the included template:
```
cp racket_stringer/settings/app.env.example racket_stringer/settings/app.env
```

Do not add sensitive information to the template.

Instead, open the new `racket_stringer/settings/app.env` with your favorite text editor, uncomment the block of environment variables that pertain to your shell, and fill out the missing values. Then, source the `app.env` file:

```source racket_stringer/settings/app.env```

Note that you'll need to re-source this file if you make changes to it. This file should be kept out of source control, and it is included in this project's `.gitignore`. Moving or renaming this file will require an update to `.gitignore` to keep it out of source control.

### Create a User
...

### Run Django Migrations
...

### Populate the Database
...

### Run the Development Server
...

## Deploying to a Server
...

## Built With
* Python 3.8.2
* PostgreSQL 12.2
* NGINX ...
* Ubuntu 20.04

## Future Ideas
* Add functionality to search historical orders

## Guides Used in Deployment
...

## License
MIT
