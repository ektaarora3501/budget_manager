# Generated by Django 2.2.2 on 2019-08-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0005_remind_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remind',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]