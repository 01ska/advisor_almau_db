from django.contrib import admin
from django.urls import path
from page.views import parse_and_save, success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', parse_and_save, name='upload_excel'),
    path('success/', success_view, name='success'),
]
