# Generated by Django 4.2.1 on 2023-05-11 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_remove_order_order_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_dt',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
    ]
