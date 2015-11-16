from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponse
from forms import WordCountForm

def word_count(request):
    if request.method == 'POST':
        form = WordCountForm(request.POST)
        if form.is_valid():
            print 'valid form'
    else:
        form = WordCountForm()

    template = Template("Test template. {{form}}")
    context = Context("TEST FORM")
    return HttpResponse(template.render(context))
