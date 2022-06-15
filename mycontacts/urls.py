"""mycontacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from repertoire.views import contact_delete, contact_detail, contact_update, contactlist, index
from users.views import login_user, logout_user, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name= "index"),
    path('contact_update/<int:id>/', contact_update , name= "contact_edit"),
    path('contact_delete/<int:id>/', contact_delete , name= "contact_delete"),
    path('contactlist', contactlist , name= "contact"),
    path('contact/<int:id>/', contact_detail , name= "contact_detail"),
    path('signup', signup , name= "signup"),
    path('login', login_user , name= "login"),
    path('logout', logout_user , name= "logout"),
]
