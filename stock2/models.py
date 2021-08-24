from django.db import models
from django.utils import timezone
from membership.models import User
from uuid import uuid4
import os
from django.core.exceptions import ValidationError


STOCK_CODE_SIZE = 6
STOCK_NAME_SIZE = 20

CONDITION_LEVEL = (
    (0, 'Deleted'),
    (1, 'Owner'),
    (2, 'Premium'),
    (3, 'Normal'),
)


def validate_file_size(value):
    file_size = value.size
    if file_size > 4096:
        raise ValidationError("The maximum file size that can be uploaded is 4 kB")
    else:
        return value


def upload_file_name(instance, filename):
    return f'kiwoom/{timezone.localdate().strftime("%y%m%d")}_{instance.cond_owner}_{uuid4()}_{filename}'


class Condition(models.Model):
    id = models.AutoField(primary_key=True)
    cond_name = models.CharField(max_length=100, null=False, blank=False)
    cond_owner = models.ForeignKey(User, to_field='username', null=True, blank=True, on_delete=models.SET_NULL)
    create_date = models.DateField(default=timezone.localdate, null=False, blank=False)
    delete_date = models.DateField(default=None, null=True, blank=True)
    file = models.FileField(upload_to=upload_file_name, validators=[validate_file_size])
    level = models.PositiveSmallIntegerField(default=1, null=False, blank=False, choices=CONDITION_LEVEL)

    def __str__(self):
        return f'{self.cond_owner} {self.cond_name}'


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    cond_id = models.ForeignKey(Condition, on_delete=models.CASCADE)
    stock_code = models.CharField(max_length=STOCK_CODE_SIZE, null=False, blank=False)
    stock_name = models.CharField(max_length=STOCK_NAME_SIZE, null=False, blank=False)
    create_date = models.DateField(default=timezone.localdate, null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cond_id', 'stock_code', 'create_date'], name='unique_reporting')
        ]

    def __str__(self):
        return f'{self.create_date} {self.stock_name} {self.cond_id}'


class Price(models.Model):
    id = models.AutoField(primary_key=True)
    stock_code = models.CharField(max_length=STOCK_CODE_SIZE, null=False, blank=False)
    stock_name = models.CharField(max_length=STOCK_NAME_SIZE, null=False, blank=False)
    high = models.PositiveIntegerField(null=False, blank=False)
    low = models.PositiveIntegerField(null=False, blank=False)
    open = models.PositiveIntegerField(null=False, blank=False)
    close = models.PositiveIntegerField(null=False, blank=False)
    volume = models.PositiveIntegerField(null=False, blank=False)
    create_date = models.DateField(default=timezone.localdate, null=False, blank=False)
    delta = models.CharField(max_length=1, null=False, blank=False,
        choices=[('D', 'Days'), ('W', 'Weeks'), ('M', 'Months')])

    def __str__(self):
        return f'{self.create_date} {self.stock_name} {self.delta} {self.close}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['stock_code', 'create_date', 'delta'], name='unique_price')
        ]


class ToWatch(models.Model):
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    stock_code = models.CharField(max_length=STOCK_CODE_SIZE, null=False, blank=False)
    stock_name = models.CharField(max_length=STOCK_NAME_SIZE, null=False, blank=False)
    create_date = models.DateField(default=timezone.localdate, null=False, blank=False)
    delete_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.username} {self.stock_name} {self.create_date} - {self.delete_date}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'stock_code'], name='unique_watching')
        ]


class ToSubscribe(models.Model):
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    cond_id = models.ForeignKey(Condition, null=True, on_delete=models.SET_NULL)
    order = models.PositiveSmallIntegerField(null=False, blank=False)
    level = models.PositiveSmallIntegerField(null=False, blank=False, choices=CONDITION_LEVEL)
    create_date = models.DateField(default=timezone.localdate, null=False, blank=False)
    delete_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.username} {self.order} {self.cond_id}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'cond_id'], name='unique_subscription_cond'),
            models.UniqueConstraint(fields=['username', 'order'], name='unique_subscription_order'),
        ]