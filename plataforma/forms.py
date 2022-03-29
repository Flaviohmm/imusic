from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Album, Musica


class NovoAlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('nome_do_album', 'genero_do_album', 'logo_do_album')


class NovaMusicaForm(forms.ModelForm):

    class Meta:
        model = Musica
        fields = ('nome_da_musica', 'arquivo_de_musica')