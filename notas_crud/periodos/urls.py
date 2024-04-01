from django.urls import path

from periodos import views

app_name = 'periodos'
urlpatterns = [
    path('', views.PeriodoList.as_view(), name='list'),
    path('create/', views.PeriodoCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.PeriodoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.PeriodoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.PeriodoDelete.as_view(), name='delete'),
]