from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title', ]
	list_display = ('id', 'title',)
	search_fields = ('id', 'title', )
	ordering = ('-created_at', )
	list_filter = ('created_at',)

admin.site.register(Product, ProductAdmin)