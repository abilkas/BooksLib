from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User


class Genre(models.Model):
	name = models.CharField("Название", max_length=50)
	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField("Имя Фамилия", max_length=50)
	was_born = models.DateField("Родился в", blank=True, null=True, help_text='Год-Месяц-День')

	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField("Название", max_length=100)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	country = models.CharField("Страна", max_length=100)
	genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
	started_date = models.DateField("Когда начали читать", blank=True, null=True, help_text='Год-Месяц-День')
	finished_date = models.DateField("Когда закончили читать", blank=True, null=True, help_text='Год-Месяц-День')
	review = models.TextField("Какое послевкусие от книги?", blank=True, null=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	quote_image = models.ImageField("Изображение", upload_to='media/', blank=True,null=True)
	#url = models.SlugField(max_length=130, unique=True)

	#def get_absolute_url(self):
	#	return reverse("book_detail", kwargs={"slug": self.url})


	def __str__(self):
		return self.name



