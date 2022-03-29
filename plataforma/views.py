from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms

from .models import Album, Musica

# Create your views here.


@login_required(login_url='/auth/login')
def home(request):
    # Mostrar todos os álbuns em ordem cronológica de upload
    albuns = Album.objects.all()
    return render(request, 'home.html', {'albuns': albuns})