# -*- encoding: utf-8 -*-
from django.db import models


class Pais(models.Model):
    codigo = models.SlugField(max_length=2,
                              unique=True)
    nombre = models.CharField(max_length=100,
                              db_index=True)
    es_hispano = models.BooleanField(default=False,
                                     db_index=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'país'
        verbose_name_plural = 'países'
    
    def __str__(self):
        return self.nombre
