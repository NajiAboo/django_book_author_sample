from operator import mod
from tabnanny import verbose
from turtle import RawTurtle
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return f"{self.name} , {self.code}"
    
    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.street},{self.postal_code},{self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="author", null=True)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_full_name()

   
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country, related_name="books")
    
    def get_absolute_url(self):
        return reverse("bookdetails", args=[self.id])
    
    def get_book_author_first_name(self):
        return self.author.first_name
    
    def get_book_author_last_name(self):
        return self.author.last_name
    
    get_book_author_first_name.short_description ="author_first_name"
    get_book_author_last_name.short_description = "author_last_name"
    
    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"