from django import forms
from .models import SocialNetwork

class SocialnetworkForm(forms.ModelForm):

    class Meta:
        model = SocialNetwork
        exclude = ()