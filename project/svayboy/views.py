from django.shortcuts import render
from .forms import CallsForm
from .models import Svayboy

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


class SvayboyDetailView(DetailView):
    model = Svayboy
    template_name = 'svayboy/svayboy_detail_view.html'
    context_object_name = 'svayboy'


def svayboy(request):
    data = call(request)
    data['svayboys'] = Svayboy.objects.all()
    return render(request, 'main/svayboy.html', data)
