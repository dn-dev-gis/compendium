from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from filter.views import home
# from filter import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # url(r'^search/$', views.home, name='main'),
]
