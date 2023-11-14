from django.urls import path
from django.contrib import admin
from ORMtest.views import hola

urlpatterns = [
 path('^admin/', admin.site.urls),
 path('hola/', hola),
]
 