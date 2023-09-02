from django.shortcuts import render
from django.views.generic import DetailView

from .forms import CallsForm
from .models import Ekskavator


def call(request):
    error = ''
    if request.method == 'POST':
        form = CallsForm(request.POST)
        if form.check():
            form.save()
            error = 'Заявка отправлена'
        else:
            error = 'Форма заполнена неверно'

    data = {
        'form': CallsForm(),
        'error': error
    }
    return data


class EkskavatorDetailView(DetailView):
    model = Ekskavator
    template_name = 'ekskavat/ekskavator_detail_view.html'
    context_object_name = 'ekskavator'


def ekskavator(request):
    data = call(request)
    data['ekskavators'] = Ekskavator.objects.all()
    return render(request, 'main/ekskavator.html', data)
