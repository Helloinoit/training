
from django import forms
from django.contrib.auth.models import User
from .models import Photo, Profile



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Profile
        model = Photo
        fields = ('photo_text', 'photo')
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(RSVPForm, self).__init__(*args, **kwargs)

class NumberForm(forms.Form):
    number_of_pages = forms.IntegerField()



class DecsriptionForm(forms.Form):
    description = forms.CharField(label='description', max_length=160)



