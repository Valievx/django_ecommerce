from django import forms
from django.utils.translation import gettext_lazy as _

from chat.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}

        widgets = {
            'message': forms.Textarea(attrs={'placeholder': _('Написать сообщение')})
        }

