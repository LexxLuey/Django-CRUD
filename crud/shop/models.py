from django.db import models
from django.db.models.deletion import CASCADE
from django.urls.base import reverse

# Create your models here.

""" 
Models for the Restuarant CRUD App
-Meals
-Category
-Menu
"""

class Category(models.Model):
    name = models.CharField(max_length=191, db_index=True)
    slug = models.SlugField(max_length=191, unique=True)

    def get_absolute_url(self):
        return reverse("shop:meal_list_by_category", args=[self.slug])
    
    class Meta:

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    

class Meal(models.Model):
    category = models.ForeignKey(Category, related_name='meals', on_delete=CASCADE)
    name = models.CharField(max_length=191, db_index=True)
    slug = models.SlugField(max_length=191, db_index=True)
    image = models.ImageField(upload_to='meals/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("shop:meal_detail", args=[self.id, self.slug])
    

    class Meta:

        ordering = ('name',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name
