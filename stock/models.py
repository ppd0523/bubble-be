from django.db import models
import datetime as dt


class Filter(models.Model):
    filter_id = models.CharField(max_length=3, unique=True)
    filter_name = models.CharField(max_length=20)
    filter_title = models.CharField(max_length=50, blank=True)
    filter_date = models.DateField()

    def __str__(self):
        return f'{self.filter_id} {self.filter_name}'


class Report(models.Model):
    filter_id = models.ForeignKey(Filter, on_delete=models.CASCADE, null=False)
    stock_code = models.CharField(max_length=10)
    stock_name = models.CharField(max_length=20)
    create_date = models.DateField()

    def __str__(self):
        return f'{self.create_date} {self.filter_id} {self.stock_name}'


class Price(models.Model):
    stock_code = models.CharField(max_length=10)
    stock_name = models.CharField(max_length=20)
    high_price = models.IntegerField()
    low_price = models.IntegerField()
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    volume = models.IntegerField()
    adj_close_price = models.IntegerField()
    create_date = models.DateField()

    def __str__(self):
        return f'{self.create_date} {self.stock_name} {self.adj_close_price}'


class DateRange(models.Model):
    begin_date = models.DateField(null=True)
    end_date = models.DateField()

    def __str__(self):
        return f'{self.begin_date} {self.end_date}'