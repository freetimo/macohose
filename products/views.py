from django.shortcuts import render
from .models import Product


def shop(request):
	products = Product.objects.all()
	ctx = {
		'products': products,
		}
	return render (request, 'shop.html', ctx)

	
def handler404(request, exception):
	return render(request, '404.html', status=404)

def handler500(request, exception):
	return render(request, '500.html', status=500)