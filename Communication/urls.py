
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from account import views as ac_views
from announce import views as an_views
from django.contrib.auth import views as au_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ac_views.home,name='home'),
    path('register/',ac_views.register,name='register'),
    path('login/',ac_views.loginfx,name='login'),
    path('logout/',ac_views.logoutfx,name='logout'),
    path('load_category/',ac_views.load_category, name='load_category'),
    path('load_departments/',ac_views.load_departments, name='load_departments'),
    path('load_levels/',ac_views.load_levels, name='load_levels'),

    path('zero/',an_views.receiver,name='zero'),
    path('mail/',ac_views.mail, name='mail'),
    path('sms/',ac_views.sms, name='sms'),
    path('sub/',ac_views.trie, name='sub'),

    path('martor/', include('martor.urls')),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    url(r'^(?P<name>[\w.@+-]+)/announce/$',an_views.announce,name='announce'),
    url(r'^(?P<name>[\w.@+-]+)/board/$',an_views.board,name='board'),
    url(r'^(?P<name>[\w.@+-]+)/board/new$',an_views.nu_announce,name='nu_announce'),
    url(r'^(?P<name>[\w.@+-]+)/announce/(?P<pky>\d+)/$',an_views.view_announce_anct,name='view_announce_anct'),
    url(r'^(?P<name>[\w.@+-]+)/board/(?P<pky>\d+)/$',an_views.view_announce_brd,name='view_announce_brd'),
    url(r'^(?P<name>[\w.@+-]+)/board/(?P<pky>\d+)/edit/$',an_views.edit_announce,name='edit'),
    url(r'^(?P<name>[\w.@+-]+)/board/(?P<pky>\d+)/delete/$',an_views.del_announce,name='delete'),

    url(r'^reset/$',
        au_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),
    name='password_reset'),
    url(r'^reset/done/$',
    au_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    au_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    url(r'^reset/complete/$',
    au_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),

    url(r'^settings/password/$', au_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', au_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)