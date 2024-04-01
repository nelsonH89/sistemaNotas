from django.urls import path

from notas import views

app_name = 'notas'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.NotaList.as_view(), name='list'),
    path('create/', views.NotaCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.NotaUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.NotaDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.NotaDelete.as_view(), name='delete'),
]