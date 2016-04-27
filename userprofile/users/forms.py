from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):
	model = UserProfile
	fields = ['likes_cheese', 'favorite_hamster_name']