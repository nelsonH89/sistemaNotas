from django.urls import path

from turnos import views

app_name = 'turnos'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.TurnoList.as_view(), name='list'),
    path('create/', views.TurnoCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.TurnoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.TurnoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.TurnoDelete.as_view(), name='delete'),
]
