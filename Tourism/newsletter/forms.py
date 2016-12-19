from django import forms
from .models import SignUp
class ContactForm(forms.Form):
	full_name=forms.CharField()
	email=forms.EmailField()
	message=forms.CharField()




class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']
	def clean_email(self):
		email =  self.cleaned_data.get('email')
		email_base , provider = email.split("@")
		domain,extension = email.split('.')
		

		return email