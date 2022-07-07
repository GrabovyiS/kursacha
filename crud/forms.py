from .models import Records
from django.forms import ModelForm, TextInput


class RecordsForm(ModelForm):
    class Meta:
        model = Records
        fields = ['city', 'date', 'temperature', 'humidity', 'windspeed']

        widgets = {
            "city": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': 'Москва',
                'id': 'city',
            }
            ),
            "date": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '20.06.2021',
                'id': 'date',
            }
            ),
            "temperature": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '28',
                'id': 'temp',
            }
            ),
            "humidity": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '83',
                'id': 'humidity',
            }
            ),
            "windspeed": TextInput(attrs={
                'class': 'form__input form-control form__input_last',
                'placeholder': '10',
                'id': 'date',
            }
            )
        }


class EditForm(ModelForm):
    class Meta:
        model = Records
        fields = ['city', 'date', 'temperature', 'humidity', 'windspeed']

        widgets = {
            "city": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': 'Москва',
                'id': 'city',
            }
            ),
            "date": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '20.06.2021',
                'id': 'date',
            }
            ),
            "temperature": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '28',
                'id': 'temp',
            }
            ),
            "humidity": TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '83',
                'id': 'humidity',
            }
            ),
            "windspeed": TextInput(attrs={
                'class': 'form__input form-control form__input_last',
                'placeholder': '10',
                'id': 'date',
            }
            )
        }
