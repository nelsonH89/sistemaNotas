from django.urls import path

from alunos import views


app_name = 'alunos'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.AlunoList.as_view(), name='list'),
    path('create/', views.AlunoCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.AlunoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.AlunoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.AlunoDelete.as_view(), name='delete'),
    
]
