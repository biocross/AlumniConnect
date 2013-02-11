from messages.msg.models import user
from django.forms import ModelForm


class mod_form_user(ModelForm):
	class Meta:
		model = user
