from django.db import models


class Contact(models.Model):
	title = models.CharField(max_length=250)
	email = models.EmailField(max_length=250)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
