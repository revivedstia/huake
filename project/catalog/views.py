from django.shortcuts import render

from .forms import CallsForm


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


def catalog(request):
    data = call(request)
    return render(request, 'main/catalog.html', data)
