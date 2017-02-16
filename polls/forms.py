from django.forms import ModelForm
from .models import Question, Choice


class Vote(ModelForm):
    class Meta:
        model = Question
