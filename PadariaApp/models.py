from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    imagem = models.BinaryField()
