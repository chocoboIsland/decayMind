# Generated by Django 2.1 on 2018-09-11 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_sys', '0009_adminuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='adminUser',
        ),
        migrations.DeleteModel(
            name='testNew',
        ),
        migrations.DeleteModel(
            name='UserAccountInfo',
        ),
    ]
