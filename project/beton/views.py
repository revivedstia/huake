from django.shortcuts import render
from django.views.generic import DetailView

from .forms import CallsForm
from .models import Beton


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


class BetonDetailView(DetailView):
    model = Beton
    template_name = 'beton/beton_detail_view.html'
    context_object_name = 'beton'

    def __int__(self, request):
        self.data = call(request)


def beton(request):
    data = call(request)
    data['beton'] = Beton.objects.all()
    return render(request, 'main/beton.html', data)
