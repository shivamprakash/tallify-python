from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from forms import WordCountForm
from django.conf import settings
def word_count(request):
    if request.method == 'POST':
        form = WordCountForm(request.POST) 
        if form.is_valid():
            print 'valid form'
    else:
        form = WordCountForm()

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'form' : form,
        'subpath' : settings.SUBPATH
    })
    return HttpResponse(template.render(context))
