from django import forms

class NumberForm(forms.Form):
    number_of_pages = forms.IntegerField()
