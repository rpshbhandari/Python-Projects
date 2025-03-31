# forms.py in accounts app

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget = forms.ClearableFileInput(
            attrs={'class': 'form-control'}
        )
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})
