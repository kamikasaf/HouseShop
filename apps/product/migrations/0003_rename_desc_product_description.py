# Generated by Django 4.0.5 on 2022-06-22 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
    ]
