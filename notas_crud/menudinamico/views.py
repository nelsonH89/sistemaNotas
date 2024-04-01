from django.shortcuts import render
from django.apps import apps
from .models import MenuList
from .serializers import menuserializer, submenuserializer

# Função para obter todas as aplicações
def get_all_apps():
    return [app.name for app in apps.get_app_configs()]

# Lista de ações
actions = ['listar', 'criar', 'atualizar', 'deletar']

# A sua view
def dynamicmenu(request):
    try:
        all_apps = get_all_apps()
        menu = []
        for app in all_apps:
            menu_item = {
                'name': app,
                'submenus': actions,
            }
            menu.append(menu_item)
        return render(request, 'index.html', {'menu': menu})
    except Exception as e:
        print(e)
        return render(request, 'error.html', {'error_message': str(e)})

