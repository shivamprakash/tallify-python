from django import forms

class WordCountForm(forms.Form):
    wordcounttext = forms.CharField(widget=forms.Textarea, required=True)
    stopwords = forms.CharField(widget=forms.Textarea)
