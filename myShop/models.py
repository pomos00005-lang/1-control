from django.db import models

# Create your models here.

class Category(models.Model):
    name_category = models.CharField(verbose_name='название котегории',max_length=100)
    
    def __str__(self):
        return self.name_category



class Product(models.Model):
    name_product = models.CharField(verbose_name='Товар:',max_length=100)
    image = models.ImageField(verbose_name='фото продукта',upload_to='products/')
    price = models.IntegerField(verbose_name='Цена продукта:')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")

    def __str__(self):
        return self.name_product