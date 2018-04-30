from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Required')
    first_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name','last_name')


class Booking_form(forms.Form):
	tier1_demand=forms.IntegerField(initial=0)
	tier2_demand=forms.IntegerField(initial=0)
	def __init__(self, *args, **kwargs):
		self.dem1 = kwargs.pop('dem1', None)
		self.dem2=kwargs.pop('dem2',None)
		super(Booking_form, self).__init__(*args, **kwargs)
	def clean(self):
		cd = self.cleaned_data
		print(self.dem1,self.dem2,cd.get('tier1_demand'),cd.get('tier2_demand'))
		if self.dem1<cd.get('tier1_demand'):
			self.add_error('tier1_demand', "You have exceeded my demand")
			return False
		if self.dem2<cd.get('tier2_demand'):
			self.add_error('tier2_demand', "You have exceeded my demand")
			return False
		return cd

	def validate1(self,dem,value1):
		print(dem,value1)
		if dem>value1:
			print("invalid")
			raise ValidationError("Invalid, must not exceed than {} ". format(value1))


	def validate2(self,dem,value2):
		if dem>value2:
			raise ValidationError("Invalid, must not exceed than {} ". format(value2))

class Modify_form(forms.Form):
	email = forms.EmailField(help_text='Required')
	first_name=forms.CharField(required=False)
	last_name=forms.CharField(required=False)
