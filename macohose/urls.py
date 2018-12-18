from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from orders import views
from products import views as p_views
from contacts import views as c_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('help_bear/', admin.site.urls),
  path('', TemplateView.as_view(template_name="index.html"), name="home"),
  path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
  path('shop/', p_views.shop, name="shop"),
  path('shop/<str:slug>/', views.shop_item, name="shop_item"),
  path('add/', views.add, name='shopping-cart-add'),
  path('remove/', views.remove, name='shopping-cart-remove'),
  path('cart/', views.cart, name='cart'),
  path('checkout/', views.checkout, name="checkout"),
  path('contact/', c_views.contact, name="contact"),
  path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
  path('<str:email>/', views.email, name="email"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
handler404 = 'products.views.handler404'
handler500 = 'products.views.handler500'
