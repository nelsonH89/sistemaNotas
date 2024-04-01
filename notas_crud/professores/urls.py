from django.urls import path

from professores import views

app_name = 'professores'
urlpatterns = [
    path('index', views.index, name='index'),
    path('list', views.ProfessorList.as_view(), name='list'),
    path('professor/<int:professor_id>/', views.ProfessorView.as_view(), name='professor_view'),
    path('create/', views.ProfessorCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ProfessorUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ProfessorDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ProfessorDelete.as_view(), name='delete'),
]
