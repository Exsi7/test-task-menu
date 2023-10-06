from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['id']


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='menu')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children'
    )
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
    
    class Meta:
        verbose_name = 'Пункт Меню'
        verbose_name_plural = 'Пункты Меню'
        ordering = ['id', 'menu_id']