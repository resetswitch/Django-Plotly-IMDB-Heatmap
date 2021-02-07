from django import forms

class NameForm(forms.Form):
    forms_url = forms.CharField(label='', 
                                max_length=100,
                                widget=forms.TextInput(attrs={'class':"form-control mr-sm-2","type":"search", "placeholder":"Insert IMDB TV link", "aria-label":"Search"}))