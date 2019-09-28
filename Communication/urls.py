
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from account import views as ac_views
from announce import views as an_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',ac_views.register,name='register'),
    path('load_category/',ac_views.load_category, name='load_category'),
    path('load_departments/',ac_views.load_departments, name='load_departments'),
    path('load_levels/',ac_views.load_levels, name='load_levels'),

    url(r'^(?P<name>[\w.@+-]+)/announce/$',an_views.announce,name='announce'),
    url(r'^(?P<name>[\w.@+-]+)/board/$',an_views.board,name='board'),
    url(r'^(?P<name>[\w.@+-]+)/board/new$',an_views.nu_announce,name='nu_announce'),
    url(r'^(?P<name>[\w.@+-]+)/board/(?P<pky>\d+)/$',an_views.view_announce,name='view_announce'),


]
