from django import forms

class WordCountForm(forms.Form):
    wordcounttext = forms.CharField(required=True)
    stopwords = forms.CharField(required=False)
