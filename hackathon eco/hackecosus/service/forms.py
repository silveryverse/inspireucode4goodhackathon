from django import forms
from .models import UploadedImage, UploadCattleImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image', 'description', 'location', 'pincode')  

class CattleImageUploadForm(forms.ModelForm):
    class Meta:
        model= UploadCattleImage
        fields=('image', 'description', 'location', 'pincode')