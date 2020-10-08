"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from restapi import views as restapiview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', restapiview.home, name = 'home'),
    path('restapi/task/string', restapiview.taskstring, name = 'restapi_task_string'),
    # path('restapi/task/xml', restapiview.taskxml, name = 'restapi_task_xml'),
    # path('restapi/task/json', restapiview.taskjson, name='restapi_task_json')
]
