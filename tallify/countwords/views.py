from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from forms import WordCountForm
from django.conf import settings
from tasks import *
def word_count(request):
    if request.method == 'POST':
        form = WordCountForm(request.POST)
        if form.is_valid():
            words = form.cleaned_data["wordcounttext"]
            stopwords = form.cleaned_data["stopwords"]
            stopwords = getStopwords(stopwords)
            print wordCount(words , stopwords)

            print 'valid form'
    else:
        form = WordCountForm()

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'form' : form,
        'subpath' : settings.SUBPATH
    })
    return HttpResponse(template.render(context))
