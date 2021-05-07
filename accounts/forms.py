from django.contrib.auth.forms import UserCreationForm
from .models import Account, AccountManager


class FormRegister(UserCreationForm):

	class Meta:
		model = Account
		fields = ['email', 'password1', 'password2']

