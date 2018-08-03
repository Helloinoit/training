from django.urls import include, path

from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    path('home/', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('<int:photo_id>/', views.detail, name='detail'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/app1/home'}, name='logout'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('upload/', views.upload, name='upload'),
]
urlpatterns += staticfiles_urlpatterns()
