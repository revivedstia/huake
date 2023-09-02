from django.shortcuts import render
from .forms import CallsForm
from .models import Vil_pogruz

from django.views.generic import DetailView


class Vil_pogruzDetailView(DetailView):
    model = Vil_pogruz
    template_name = 'vil_pogruz/vil_pogruz_detail_view.html'
    context_object_name = 'vil_pogruz'


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


def vil_pogruz(request):
    data = call(request)
    data['vil_pogruz'] = Vil_pogruz.objects.all()
    return render(request, 'main/vil_pogruz.html', data)

