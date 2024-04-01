from django.urls import path

from matriculas import views

app_name = 'matriculas'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.MatriculaList.as_view(), name='list'),
    path('create/', views.MatriculaCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.MatriculaUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.MatriculaDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.MatriculaDelete.as_view(), name='delete'),
]
