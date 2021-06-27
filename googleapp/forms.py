from django.forms import ModelForm
from .models import log
class Message(ModelForm):
    class Meta:
     model=log

     fields="__all__"
