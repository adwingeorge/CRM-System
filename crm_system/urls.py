from django.contrib import admin
from django.urls import path, include
from . import views
from accounts.views import api_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/login/', api_login, name='api_login'),
    path('', views.serve_react_app, name='home'),
]