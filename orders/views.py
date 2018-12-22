from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Order
from django.http import JsonResponse, HttpResponse
from carton.cart import Cart
from products.models import Product
from django.utils import timezone
from datetime import timedelta

def shop_item(request, slug):
	product = get_object_or_404(Product, slug=slug)
	ctx = {
		'product': product,
		}
	return render(request, 'shop_item.html', ctx)

def add(request):
	cart = Cart(request.session)
	pk = request.POST.get('pk')
	quantity = request.POST.get('quantity')
	if quantity == '':
		message = '수량을 선택해주세요.'
		ctx = {'message': message, }
		return JsonResponse(ctx)
	else:
		product = Product.objects.get(id=pk)
		if not product.category == 'EXTRA':
			cart.add(product, price=product.price, quantity=quantity)
			total_count = cart.count
			message = '장바구니에 상품을 담았습니다.'
			ctx = {'message': message, 'total_count': total_count,}
			return JsonResponse(ctx)
		else:
			cart.add(product, price=product.price, quantity=quantity)
			for cart_item in cart.items:
				if cart_item.product.title == product.title:
					if cart_item.quantity > 5:
						cart.set_quantity(product, quantity=5)
						total_count = cart.count
						message = 'EXTRA 상품은 최대 5개까지 구매하실 수 있습니다.'
						ctx = {'message': message, 'total_count': total_count,}
						return JsonResponse(ctx)
					else:
						total_count = cart.count
						message = '장바구니에 상품을 담았습니다.'
						ctx = {'message': message, 'total_count': total_count,}
						return JsonResponse(ctx)

def remove(request):
	cart = Cart(request.session)
	product = Product.objects.get(id=request.GET.get('id'))
	cart.remove(product)
	return redirect('cart')  

def cart(request):
	cart = Cart(request.session)
	total_count = cart.count
	coffee_list = []
	coffee_count = 0
	for cart_item in cart.items:
		if cart_item.product.category == 'COFFEE':
			coffee_count += cart_item.quantity
			coffee_list.append(cart_item.product)
	if len(coffee_list) > 0:
		status = True
		if coffee_count > 2:
			total_cost = cart.total
			ctx = {'total_cost': total_cost, 'cart': cart, 'status': status,}
			return render(request, 'cart.html', ctx)
		else:
			total_cost = cart.total + 2500
			message = "커피 세 상자 이상 구매시 배송비 무료입니다."
			ctx = {'total_cost': total_cost, 'cart': cart, 'message': message, 'status': status,}
			return render(request, 'cart.html', ctx)
	else:
		status = False
		total_cost = cart.total + 2500
		message = "EXTRA 상품만 구매하실 수 없습니다."
		ctx = {'total_cost': total_cost, 'cart': cart, 'message': message, 'status': status,}
		return render(request, 'cart.html', ctx)

def checkout(request):
	cart = Cart(request.session)
	total_count = cart.count
	order_list = []
	coffee_list = []
	coffee_count = 0
	for item in cart.items:
		order_list.extend([item.product.title, item.quantity])
		if item.product.category == 'COFFEE':
			coffee_count += item.quantity
			coffee_list.append(item.product)
	if len(coffee_list) > 0:
		status = True
		if coffee_count < 3:
			total_cost = cart.total + 2500
			if request.method == 'POST':
				form = PostForm(request.POST)
				if form.is_valid():
					checkout = form.save(commit=False)
					checkout.total_product = order_list
					checkout.total_price = total_cost
					checkout.save()
					cart.clear()
					return redirect('email', email=checkout.email)
				else:
					ctx = {'form': form, 'cart': cart, 'coffee_count': coffee_count, 'total_cost': total_cost, 'status': status,}
					return render(request, 'checkout.html', ctx)
			else:
				form = PostForm()
				ctx = {'form': form, 'cart': cart, 'coffee_count': coffee_count, 'total_cost': total_cost, 'status': status,}
				return render(request, 'checkout.html', ctx)
		else:
			total_cost = cart.total
			if request.method == 'POST':
				form = PostForm(request.POST)
				if form.is_valid():
					checkout = form.save(commit=False)
					checkout.total_product = order_list
					checkout.total_price = total_cost
					checkout.save()
					cart.clear()
					return redirect('email', email=checkout.email)  
				else:
					ctx = {'form': form, 'cart': cart, 'coffee_count': coffee_count, 'total_cost': total_cost, 'status': status,}
					return render(request, 'checkout.html', ctx)
			else:
				form = PostForm()
				ctx = {'form': form, 'cart': cart, 'total_cost': total_cost, 'status': status,}
				return render(request, 'checkout.html', ctx)
	else:
		total_cost = cart.total + 2500
		message = "EXTRA 상품만 구매하실 수 없습니다."
		status = False
		form = PostForm()
		ctx = {'form': form, 'cart': cart, 'total_cost': total_cost, 'message': message, 'status': status,}
		return render(request, 'checkout.html', ctx)

def email(request, email):
	now = timezone.localtime()
	enddate = now - timedelta(days=2)
	orders = Order.objects.filter(email=email, created_at__gte=enddate)
	ctx = {'orders': orders, 'email': email,}
	return render(request, 'order.html', ctx)
