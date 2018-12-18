from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'name', 'total_price', 'total_product',]
	list_display = ('id', 'money', 'deliver', 'name', 'total_price', 'total_product', 'zipcode', 'address', 'detail_address', 'created_at',)
	search_fields = ('name', )
	ordering = ('-created_at', )
	list_filter = ('created_at',)

admin.site.register(Order, OrderAdmin)