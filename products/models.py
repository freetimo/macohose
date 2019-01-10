from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.timezone import now


class Product(models.Model):
	title = models.CharField(max_length=250)
	category = models.CharField(max_length=250, blank=True)
	info = models.CharField(max_length=250, blank=True)
	price = models.PositiveIntegerField(blank=True,)
	slug = models.SlugField(allow_unicode=True, default='')
	thumbnail = ProcessedImageField(
		upload_to='shop/thumbnail/', 
		blank=True,
		processors=[ResizeToFill(700, 700)],
	)
	content1 = ProcessedImageField(
		upload_to='shop/thumbnail/', 
		blank=True,
	)
	content2 = ProcessedImageField(
		upload_to='shop/thumbnail/', 
		blank=True,
	)
	content3 = ProcessedImageField(
		upload_to='shop/thumbnail/', 
		blank=True,
	)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['id']
		

class Review(models.Model):
	title = models.CharField(max_length=250)
	category = models.CharField(max_length=250, blank=True)
	star = models.PositiveIntegerField()
	description = models.TextField()
	created_at = models.DateTimeField(default=now)

	class Meta:
		ordering = ['-created_at']