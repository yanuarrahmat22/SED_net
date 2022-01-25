from django import forms
from django.forms import widgets
from django.core.files import File
from PIL import Image
from .models import *
  
class imageForm(forms.ModelForm):
    class Meta:
        model = Image_Upload
        fields = ['name_Img']

        labels = {
			'name_Img':'Choose Image File Here: ',
		}

        widgets = {
            'name_Img': forms.FileInput(
                attrs={
                    'class':'form-control border-0'
                }
            )
        } 