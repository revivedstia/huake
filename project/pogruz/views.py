from django.shortcuts import render
from .forms import CallsForm
from .models import Pogruz

from django.views.generic import DetailView


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


class PogruzDetailView(DetailView):
    model = Pogruz
    template_name = 'pogruz/pogruz_detail_view.html'
    context_object_name = 'pogruz'


def pogruz(request):
    data = call(request)
    data['pogruzs'] = Pogruz.objects.all()
    return render(request, 'main/pogruz.html', data)
