from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CustomUserForm
from .models import CustomUser 


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = request.POST.get('user_type')
            user.customuser.user_type = user_type
            user.customuser.save()
            messages.success(request, f'Conta criada para {user.username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def index(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'users/index.html', {'usuarios': usuarios})

def update_user(request, user_id):
    usuario = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:index'))
    else:
        form = CustomUserForm(instance=usuario)
    return render(request, 'users/update_user.html', {'form': form})

def delete_user(request, user_id):
    usuario = get_object_or_404(CustomUser, pk=user_id)
    usuario.delete()
    return HttpResponseRedirect(reverse('users:index'))