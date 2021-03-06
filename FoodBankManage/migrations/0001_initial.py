# Generated by Django 3.0.4 on 2020-04-11 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockname', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FoodBankBeneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField()),
                ('head_of_family', models.CharField(max_length=50)),
                ('total_members_in_family', models.PositiveIntegerField()),
                ('mobile', models.CharField(max_length=50)),
                ('NFSA', models.BooleanField()),
                ('food_packet_Count', models.PositiveIntegerField()),
                ('wheat_kg', models.PositiveIntegerField()),
                ('rice_kg', models.PositiveIntegerField()),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodBankManage.Block')),
            ],
        ),
        migrations.CreateModel(
            name='GramPanchayat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gramname', models.CharField(max_length=128)),
                ('members', models.ManyToManyField(through='FoodBankManage.FoodBankBeneficiary', to='FoodBankManage.Block')),
            ],
        ),
        migrations.AddField(
            model_name='foodbankbeneficiary',
            name='gram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodBankManage.GramPanchayat'),
        ),
    ]
