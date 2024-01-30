from django.db import models

# Create your models here.
from django.db.models import Model


class OrderInfo(Model):

    ORDER_PAYMENT_WAYS = (
        (1, "alipay"),
        (2, "cash"),
    )
    ORDER_STATUS = (
        (1, "待支付 "),
        (2, "已支付"),
        (3, "已取消"),
    )
    users = models.ForeignKey("userapp.Users", on_delete=models.SET_NULL, related_name='consumer', null=True)
    pay_method = models.IntegerField(choices=ORDER_PAYMENT_WAYS, null=False, default=1)
    pay_status = models.IntegerField(choices=ORDER_STATUS, null=False, default=1)
    goods = models.ForeignKey('shop.GoodModule', on_delete=models.SET_NULL, related_name='seller', null=True)
    total_count = models.IntegerField(verbose_name='支付总金额')
    order_id = models.CharField(max_length=64, primary_key=True)

    class Meta:
        db_table = 't_order'
        verbose_name = 'orders'
        verbose_name_plural = verbose_name


class Payment(Model):

    trade_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    orders = models.ForeignKey('OrderInfo', on_delete=models.CASCADE,  related_name='payment')

    class Meta:
        db_table = 't_payment'
        verbose_name = 'payment'
        verbose_name_plural = verbose_name
