# Generated by Django 4.0.5 on 2022-07-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
