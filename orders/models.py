from django.db import models


class Order(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	total_price = models.PositiveIntegerField()
	total_product = models.TextField()
	zipcode = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	detail_address = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	money = models.BooleanField(default=False)
	deliver = models.BooleanField(default=False)


	class Meta:
		ordering = ['-created_at']
		
