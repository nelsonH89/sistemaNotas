from django.urls import path

from .views import base_admin


app_name = 'pages'
urlpatterns = [
    path('', base_admin, name='dashboard'),
]
