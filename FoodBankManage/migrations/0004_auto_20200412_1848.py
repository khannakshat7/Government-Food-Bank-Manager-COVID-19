# Generated by Django 3.0.4 on 2020-04-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodBankManage', '0003_auto_20200412_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodbankbeneficiary',
            name='block',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='foodbankbeneficiary',
            name='gram',
            field=models.CharField(max_length=50),
        ),
    ]