from django.urls import path

from anos_letivos import views

app_name = 'anos_letivos'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.AnoLetivoList.as_view(), name='list'),
    path('view_anoletivo/<int:pk>/', views.AnoLetivoDetailView.as_view(), name='view_anoletivo'),
    path('create/', views.AnoLetivoCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.AnoLetivoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.AnoLetivoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.AnoLetivoDelete.as_view(), name='delete'),
]
