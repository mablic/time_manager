from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeApp.urls')),
]
