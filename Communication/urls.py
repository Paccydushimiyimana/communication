
from django.contrib import admin
from django.urls import path
from account import views as ac_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',ac_views.register,name='register'),
    path('load_category/',ac_views.load_category, name='load_category'),
    path('load_departments/',ac_views.load_departments, name='load_departments'),
    path('load_levels/',ac_views.load_levels, name='load_levels'),
]
