from django import forms
from .models import Profile


class ProfileUserFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('sen','id_number','phone','bio','gener','is_writor',\
            'file_resome')
    
