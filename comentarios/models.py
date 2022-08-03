from django.db import models
from posts.models import Post
from django.utils import timezone
from django.contrib.auth.models import User


class Cometario(models.Model):
    nome_comentario = models.CharField(max_length=255, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE,verbose_name='Selecione o Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Selecione o Usuário')
    data_comentario = models.DateTimeField(default=timezone.now,verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario
# Create your models here.
