# I. Requset & Resopens

Create requests and responses in `views.py` (1)<br>
Create file `urls` (2) for `home` (3) app<br>
Config `urls` (4) for main

```
├── ProjectBase/
│   ├── home/ (3)
│   │   ├── views.py (1)
│   │   ├── urls.py (2)
│   │   └── ...
│   ├── ProjectBase/
│   │   └── urls.py (4)
│   └── ...
└── ...
```

Import requests and responses from django

```
from django.shortcuts import render
from django.http import HttpResponse
```

Example:

```
# client request -> show home
def reqHome(request):
    return render(request, 'home.html')
```

Config `urls` for `home` app:

```
from django.contrib import admin
from django.urls import path,inculed
from . import views
urlpatterns = [
    path('',views.reqHome)
]
```

Config `urls` for `ProjectBase`:

```
from django.contrib import admin
from django.urls import path, include
from home import views as home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', include('home.urls'))
]
```
