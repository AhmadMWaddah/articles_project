from django.db import models
from accounts.models import Account


class Article(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField()
	intro = models.TextField()
	content = models.TextField()
	account = models.ForeignKey(Account, on_delete=models.CASCADE, default=True)
	time_stamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-time_stamp']