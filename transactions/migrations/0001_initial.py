# Generated by Django 5.0.4 on 2024-09-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('transaction_time', models.DateTimeField()),
                ('item_code', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=5000)),
                ('quantity_items', models.IntegerField()),
                ('item_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
