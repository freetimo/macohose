from django import forms
from .models import Order

class PostForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'zipcode', 'address', 'detail_address']
