from django.shortcuts import render

from .forms import CallsForm


# from .models import Cars


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


def index(request):
    data = call(request)
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def politic(request):
    return render(request, 'main/politic.html')

# def catalog(request):
#     # data = call(request)
#     # data['form'] = CallsForm()
#     # data['cars'] = Cars.objects.all()
#     # data = {
#     #         'cars': Cars.objects.all()
#     #     }
#     return render(request, 'main/catalog.html')
