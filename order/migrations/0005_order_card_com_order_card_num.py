# Generated by Django 4.2.1 on 2023-07-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_option_menu_option_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='card_com',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='card_num',
            field=models.CharField(max_length=100, null=True),
        ),
    ]