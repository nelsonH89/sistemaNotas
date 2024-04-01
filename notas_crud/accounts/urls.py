from django.urls import path
from .views import logout_view

urlpatterns = [
    # suas outras urls aqui
    path('logout/', logout_view, name='logout'),
]
