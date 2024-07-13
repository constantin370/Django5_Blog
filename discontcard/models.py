from django.db import models


class DiscontCard(models.Model):
    """Модель Скидочной Карты"""
    number = models.BigIntegerField(verbose_name="Номер скидочной карты",
                                    unique=True)
    data_creation = models.DateField(auto_now=True,
                                     verbose_name="Дата создания")
    procent = models.DecimalField(verbose_name="Процент скидки",
                                  max_digits=3, 
                                  decimal_places=2,
                                  default=0)
    is_active = models.BooleanField(default=True,
                                    verbose_name="Статус карты")

    def __str__(self) -> str:
        return str(self.number)
    
    class Meta:
        verbose_name = "Дисконтная Карта"
        verbose_name_plural = "Дисконтные Карты"