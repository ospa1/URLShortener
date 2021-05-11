from django.forms import *
from url_shorts.models import Input


class InputForm(ModelForm):
    url = CharField(max_length=10000)

    class Meta:
        model = Input
        fields = ['url']
        labels = {'text': ''}
