from .models import Calls
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class CallsForm(ModelForm):
    class Meta:
        model = Calls
        fields = ['name', 'phone_number', 'email', 'message']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control ',
                'placeholder': '* Имя'
            }),
            'phone_number':  NumberInput(attrs={
                'class': 'form-control ',
                'placeholder': '* Телефон'
            }),
            'email': TextInput(attrs={
                'class': 'form-control ',
                'placeholder': '* Email'
            }),
            'message': Textarea(attrs={
                'class': 'form-control ',
                'id': "mess",
                'placeholder': 'Сообщение'
            })
        }

    def check(self):
        if self.data.dict()['name'] and self.data.dict()['email'] and self.data.dict()['phone_number'] \
                and '@' in self.data.dict()['email'] and len(self.data.dict()['phone_number']) == 11:
            return True
        else:
            return False
