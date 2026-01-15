from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    UNIT_CHOICES = [
        ('g', 'г'),
        ('ml', 'мл'),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='dishes'
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', blank=True)

    portion_size = models.PositiveIntegerField(
        verbose_name="Вага / обʼєм порції"
    )
    unit = models.CharField(
        max_length=2,
        choices=UNIT_CHOICES,
        default='g',
        verbose_name="Одиниця виміру"
    )

    def __str__(self):
        return self.name
