from django.urls import path

from trimestres import views

app_name = 'trimestres'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/', views.TrimestreList.as_view(), name='list'),
    path('create/', views.TrimestreCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.TrimestreUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.TrimestreDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.TrimestreDelete.as_view(), name='delete'),
]