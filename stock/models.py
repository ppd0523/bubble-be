from django.db import models


class Filter(models.Model):
    condition_name = models.CharField(max_length=50)
    create_date = models.DateField()
    stock_code = models.CharField(max_length=10, null=True, blank=True)
    stock_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.create_date} {self.stock_name}'
