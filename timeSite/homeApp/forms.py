from django import forms
from .models import List, Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ProjectForm(forms.ModelForm):
	entry_hour = forms.DecimalField(required=True, max_digits=5, decimal_places=2)

	class Meta:
		model = Project
		fields = ["entry_hour"]

class ListForm(forms.ModelForm):
	item = forms.CharField(required=True)
	# curr_user = forms.ModelChoiceField(queryset=User.objects.all())

	class Meta:
		model = List
		fields = ["item"]

	# def save(self, commit=True):
	# 	List = super(ListForm, self).save(commit=False)
	# 	if commit:
	# 		List.save()
	# 	return List

	def clean_item(self):
		item = self.cleaned_data.get('item')
		if item == '':
			raise forms.ValidationError("Invalid name!")
		else:
			return item