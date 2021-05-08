from django.db import models


class Filter(models.Model):
    filter_id = models.CharField(max_length=10)
    filter_name = models.CharField(max_length=50)
    stock_code = models.CharField(max_length=10, null=True, blank=True)
    stock_name = models.CharField(max_length=50, null=True, blank=True)
    create_date = models.DateField()

    def __str__(self):
        return f'{self.filter_id} {self.create_date} {self.stock_code} {self.stock_name[:4]}'
