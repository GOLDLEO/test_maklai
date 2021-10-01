from django.db import models

# Create your models here.

class Text(models.Model):
	full_text = models.TextField()

	def __str__(self):
		return f'{self.full_text}'

class DetailText(models.Model):
	text_id = models.ForeignKey(Text, on_delete=models.CASCADE)
	text = models.CharField(max_length=120, default='')
	pos = models.CharField(max_length=120, default='')
	tag = models.CharField(max_length=120, default='')
