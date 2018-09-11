from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    accountMoney=models.FloatField(verbose_name="账户余额",default=10000.0)
    holdStock=models.CharField(max_length=128,default='0',verbose_name="持股")
    accountStrategy=models.CharField(max_length=128,default='0',verbose_name="资金策略")
    InvestStrategy = models.CharField(max_length=128, default='0',verbose_name="投资策略")
    kidney=models.CharField(max_length=128, default='0',verbose_name="性格")
    Compatibility=models.CharField(max_length=128, default='0',verbose_name="相性")









