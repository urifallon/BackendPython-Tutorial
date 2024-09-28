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
