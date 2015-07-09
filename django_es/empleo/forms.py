# -*- encoding: utf-8 -*-
from django import forms
from .models import Oferta


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['titulo',
                  'empresa',
                  'ciudad',
                  'pais',
                  'descripcion',
                  'remuneracion',
                  'url',
                  'contacto',
                  'email']
