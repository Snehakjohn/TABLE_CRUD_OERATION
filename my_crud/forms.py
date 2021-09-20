from django.forms import ModelForm
from .models import *

class PlayForm(ModelForm):
	class Meta:
		model= Player
		fields="__all__"