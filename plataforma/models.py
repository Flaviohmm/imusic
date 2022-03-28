import os
import django
from django.db import models
from django.contrib.auth.models import User
from imusic.settings import MEDIA_ROOT

# Função que indica o caminho do diretório do usuário
def user_directory_path(self, filename):
    # Arquivo será carregado para MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.artista_do_album.id, filename)


# Função que indica o caminho do diretório do usuário da música
def user_directory_path_song(self, filename):
    # Arquivo será carregado para MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(self.album_da_musica.artista_do_album.id, filename)


# Create your models here.
class Album(models.Model):
    nome_do_album = models.CharField(max_length=30)
    carregado_em = models.DateField(default=django.utils.timezone.now)
    logo_do_album = models.FileField(upload_to=user_directory_path)
    genero_do_album = models.CharField(max_length=30)
    artista_do_album = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albuns')

    def __str__(self):
        return self.nome_do_album

    def delete_media(self):
        os.remove(path=MEDIA_ROOT + '/' + str(self.logo_do_album))

    
class Musica(models.Model):
    nome_da_musica = models.CharField(max_length=40)
    album_da_musica = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    arquivo_de_musica = models.FileField(upload_to=user_directory_path_song)

    def __str__(self):
        return self.nome_da_musica + ' - ' + str(self.album_da_musica)

    def delete_media(self):
        os.remove(path=MEDIA_ROOT + '/' + str(self.arquivo_de_musica))