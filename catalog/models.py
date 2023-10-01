from datetime import datetime

from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    description= models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.TextField(verbose_name='описание')
    avatar = models.ImageField(upload_to='products/', verbose_name='изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория',**NULLABLE)
    price = models.FloatField(verbose_name='цена за покупку')
    quantity_product = models.IntegerField(verbose_name='количество', default=0)
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y")
    date_create = models.DateField(verbose_name='дата создания', default=current_time)
    date_last_change = models.DateField(verbose_name='дата последнего изменения',default=current_time)

    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
