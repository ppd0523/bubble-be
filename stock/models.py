from django.db import models


class Filter(models.Model):
    filter_id = models.CharField(max_length=3, unique=True)
    filter_name = models.CharField(max_length=20)
    filter_title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.filter_id} {self.filter_name}'


class Report(models.Model):
    filter_id = models.ForeignKey(Filter, on_delete=models.CASCADE, null=False)
    stock_code = models.CharField(max_length=10, null=True, blank=True)
    stock_name = models.CharField(max_length=20, null=True, blank=True)
    create_date = models.DateField()

    def __str__(self):
        return f'{self.create_date} {self.filter_id} {self.stock_name}'


class Price(models.Model):
    stock_code = models.CharField(max_length=10)
    high_price = models.FloatField()
    low_price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.FloatField()
    adj_close_price = models.FloatField()
    create_date = models.DateField()

    def __str__(self):
        return f'{self.stock_code} {self.open_price} {self.close_price}'
