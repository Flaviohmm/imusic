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
from django.utils import timezone


from .models import Album, Musica
from .forms import NovoAlbumForm, NovaMusicaForm

# Create your views here.


@login_required(login_url='/auth/login')
def home(request):
    # Mostrar todos os álbuns em ordem cronológica de upload
    albuns = Album.objects.all()
    return render(request, 'home.html', {'albuns': albuns})


@login_required(login_url='/auth/login')
def detalhe_perfil(request, username):
    # Mostrar todos os álbuns do artista
    albuns = get_object_or_404(User, username=username)
    albuns = albuns.albuns.all()
    return render(request, 'informacao_artista.html', {'albuns': albuns, 'username': username})


@login_required(login_url='/auth/login')
def adicionar_album(request, username):
    user = get_object_or_404(User, username=username)
    # Somente o usuário conectado no momento pode adicionar a álbum, senão será redirecionado para a página inicial.
    if user == request.user:
        if request.method == 'POST':
            form = NovoAlbumForm(request.POST, request.FILES)
            if form.is_valid():
                album = Album.objects.create(
                    logo_do_album = form.cleaned_data.get('logo_do_album'),
                    nome_do_album = form.cleaned_data.get('nome_do_album'),
                    genero_do_album = form.cleaned_data.get('genero_do_album'),
                    carregado_em = timezone.now(),
                    artista_do_album = request.user
                )
                return redirect('plataforma:detalhe_perfil', username=request.user)
        else:
            form = NovoAlbumForm()
        return render(request, 'criar_novo_album.html', {'form': form})
    else:
        return redirect('plataforma:detalhe_perfil', username=user)


@login_required(login_url='/auth/login')
def detalhe_album(request, username, album):
    # Mostre os detalhes do álbum aqui. detalhes do único álbum.
    album = get_object_or_404(Album, nome_do_album=album)
    musicas = get_object_or_404(User, username=username)
    musicas = musicas.albuns.get(nome_do_album=str(album))
    musicas = musicas.musicas.all()
    return render(request, 'informacao_album.html', {'musicas': musicas, 'album': album, 'username': username})


@login_required(login_url='/auth/login')
def deletar_album(request, username, album):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        album_para_deletar = get_object_or_404(User, username=username)
        album_para_deletar = album_para_deletar.albuns.get(nome_do_album=album)
        musica_para_deletar = album_para_deletar.musicas.all()
        for musica in musica_para_deletar:
            musica.delete_media()           # Exclui o arquivo de música
        album_para_deletar.delete_media()   # Exclui a logo do álbum
        album_para_deletar.delete()         # Exclui o álbum do banco de dados
        return redirect('plataforma:detalhe_perfil', username=username)
    else:
        return redirect('plataforma:detalhe_perfil', username=username)