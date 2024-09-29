# I. Init Project

## Download frameworks for python website

```
pip install django
```

## Create a project

Change `<name>` by your name <br>
Change `<port>` by your port want to use in the project

```
django-admin startproject <name>    # Create a project "ProjectBase"

cd <name>                           # Move to your project "ProjectBase"

python manage.py migrate            # Init project base

python manage.py runserver <port>   # Run server "3001"

python manage.py createsuperuser    # Create role user
                                    # admin
                                    # 123

python manage.py startapp <name>    # Create modul "home"
```

## Setup folders structure

Create folder templates and `home.html` (1)<br>
Create def action templates (2) <br>
Add view to `INSTALLED_APPS` in settings (3)<br>
Import views and add path into urls (4)

```
├── ProjectBase/
│   ├── home/
│   │   ├── Templates/
│   │   │   └── home.html (1)
│   │   ├── views.py (2)
│   │   └── ...
│   ├── ProjectBase/
│   │   ├── settings.py (3)
│   │   ├── urls.py (4)
│   │   └── ...
│   └── ...
└── ...
```

<br>

# II. Init Database

Config database in `settings.py` file (1)

```
├── ProjectBase/
│   ├── home/
│   ├── ProjectBase/
│   │   ├── settings.py (1)
│   │   └── ...
│   └── ...
└── ...
```

## MySQL

Install MySQL for your project<br>

```
pip install pymysql
pip install mysqlclient
```

This MySQL using in the local database with `Xampp`

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "home",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}
```

If has errors you can try add this in to project (2):

```
├── ProjectBase/
│   ├── home/
│   │   └── _init_.py (2)
│   └── ...
└── ...
```

```
import pymysql
pymysql.install_as_MySQLdb()
```

## Sqlite

Open `DB browser` to query in sqlite database

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```
