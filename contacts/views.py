from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, '보냈습니다.')
			return redirect('contact')  
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form, })