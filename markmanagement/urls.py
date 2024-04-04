
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('',include('django.contrib.auth.urls')),
    path('',views.home,name="home"),
    path('manage/',include('teachers.urls')),

]
