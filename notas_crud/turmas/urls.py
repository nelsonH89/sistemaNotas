from django.urls import path

from turmas import views

app_name = 'turmas'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.TurmaList.as_view(), name='list'),
    path('view_turma/<int:pk>/', views.TurmaDetailView.as_view(), name='view_turma'),
    path('create/', views.TurmaCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.TurmaUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.TurmaDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.TurmaDelete.as_view(), name='delete'),
]
