from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category


class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series	


class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())

	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.tutorial_title

class List(models.Model):
	item = models.CharField(max_length=200, blank=True)
	curr_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

	def __str__(self):
		return self.item

class Project(models.Model):
	entry_date = models.DateTimeField(auto_now=True)
	entry_hour = models.DecimalField(default=0, max_digits=5, decimal_places=2)

	entry_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
	entry_project = models.ForeignKey(List, on_delete=models.CASCADE, default=0)

	def __str__(self):
		return self.entry_date.strftime("%m:%d:%Y")