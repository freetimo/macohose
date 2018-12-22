from django.shortcuts import render
from .models import Product


def shop(request):
	coffee_list = []
	extra_list = []
	for product in Product.objects.all():
		if product.category == 'COFFEE':
			coffee_list.append(product)
		if product.category == 'EXTRA':
			extra_list.append(product)
	ctx = {
		'coffee_list': coffee_list,
		'extra_list': extra_list,
		}
	return render (request, 'shop.html', ctx)

	
def handler404(request, exception):
	return render(request, '404.html', status=404)

def handler500(request, exception):
	return render(request, '500.html', status=500)