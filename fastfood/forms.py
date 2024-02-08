from django import forms

from .models import BookTable


class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ['name', 'phone', 'email', 'date', 'time', 'number_of_people', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'number_of_people': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Necha kishi'}, choices=[(i, i) for i in range(1, 11)]),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabar'}),
        }
