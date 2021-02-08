from django import forms

#https://docs.djangoproject.com/en/3.1/ref/forms/fields/
class NameForm(forms.Form):
    forms_url = forms.URLField(label='', 
                                max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class':"form-control mr-sm-2","type":"search", "placeholder":"Insert IMDB TV link", "aria-label":"Search"}))