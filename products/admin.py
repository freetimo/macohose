from django.contrib import admin
from .models import Product, Review

class ProductAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title', ]
	list_display = ('id', 'title',)
	search_fields = ('id', 'title', )
	ordering = ('-created_at', )
	list_filter = ('created_at',)


class ReviewAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'category', 'title', 'description']
	list_display = ('id', 'category', 'title', 'description')
	search_fields = ('id', 'title', 'description')
	ordering = ('-created_at', )
	list_filter = ('created_at',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)