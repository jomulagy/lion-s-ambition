# Generated by Django 4.2.1 on 2023-05-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_category1_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category1',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menues', to='category.type'),
        ),
    ]
