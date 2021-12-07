from django import forms
from django.forms import widgets



class SearchForm(forms.Form):

    search_terms = forms.CharField(strip=True, label="", max_length=250,min_length=0,empty_value="", widget=forms.TextInput(attrs={"class":'form-control search-form nav-link', 'placeholder':"Rechercher..."}))
