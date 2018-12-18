from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display_links = ['id', 'title', 'description',]
	list_display = ('id', 'title', 'description', 'created_at',)
	search_fields = ('title', 'description', )
	ordering = ('-created_at', )
	list_filter = ('created_at',)

admin.site.register(Contact, ContactAdmin)