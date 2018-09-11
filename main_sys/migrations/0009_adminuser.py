# Generated by Django 2.1 on 2018-09-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_sys', '0008_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('accountMoney', models.FloatField(default=10000.0, verbose_name='账户余额')),
                ('holdStock', models.CharField(default='0', max_length=128, verbose_name='持股')),
                ('accountStrategy', models.CharField(default='0', max_length=128, verbose_name='资金策略')),
                ('InvestStrategy', models.CharField(default='0', max_length=128, verbose_name='投资策略')),
                ('kidney', models.CharField(default='0', max_length=128, verbose_name='性格')),
                ('Compatibility', models.CharField(default='0', max_length=128, verbose_name='相性')),
            ],
        ),
    ]
