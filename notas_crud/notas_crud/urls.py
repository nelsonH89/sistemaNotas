"""
URL configuration for notas_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('menudinamico.urls')),
    path('dashboard/', include('pages.urls')),
    path("admin/", admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/", include('accounts.urls')),
    path("alunos/", include('alunos.urls')),
    path("professores/", include('professores.urls')),
    path("disciplinas/", include('disciplinas.urls')),
    path("turmas/", include('turmas.urls')),
    path("periodos/", include('periodos.urls')),
    path("notas/", include('notas.urls')),
    path("anos_letivos/", include('anos_letivos.urls')),
    path("trimestres/", include('trimestres.urls')),
    path("turnos/", include('turnos.urls')),
    path("matriculas/", include('matriculas.urls')),
    path("users/", include('users.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)