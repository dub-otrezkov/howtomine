from typing import Any, Mapping, Optional, Type, Union
from django.forms import *
from django.forms.utils import ErrorList
from .models import *

class ChooseCardForm(Form):
    cards = ChoiceField(label="", choices=((i, VideoCard.objects.all()[i].name) for i in range(len(VideoCard.objects.all()))))

        # self.cards.choices = tuple(tmp_l)