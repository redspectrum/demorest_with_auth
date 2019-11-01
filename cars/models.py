from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True,unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'Sedan'),
        (2, 'Hatchback'),
        (3, 'Universal'),
        (4, 'Coupe'),
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)