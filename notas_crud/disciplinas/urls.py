from django.urls import path

from disciplinas import views

app_name = 'disciplinas'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.DisciplinaList.as_view(), name='list'),
    path('create/', views.DisciplinaCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.DisciplinaUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.DisciplinaDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DisciplinaDelete.as_view(), name='delete'),
]
