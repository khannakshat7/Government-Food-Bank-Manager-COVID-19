# Generated by Django 3.0.4 on 2020-04-14 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodBankManage', '0005_foodbankinventrycook_foodbankinventrydry_foodbankinventrymid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodbankinventrycook',
            old_name='Available',
            new_name='Distributed_Overall_Cooked_Meal',
        ),
        migrations.RenameField(
            model_name='foodbankinventrycook',
            old_name='Distributed',
            new_name='Received_Cooked_Meal_Bhamashah',
        ),
        migrations.RenameField(
            model_name='foodbankinventrycook',
            old_name='Recieved_Bhamashah',
            new_name='Received_Cooked_Meal_Government',
        ),
        migrations.RenameField(
            model_name='foodbankinventrycook',
            old_name='Recieved_Government',
            new_name='Recieved_Cooked_Meal_NGO',
        ),
        migrations.RemoveField(
            model_name='foodbankinventrycook',
            name='Recieved_NGO',
        ),
        migrations.RemoveField(
            model_name='foodbankinventrycook',
            name='Required',
        ),
    ]
