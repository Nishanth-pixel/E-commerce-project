# Generated by Django 5.1.4 on 2025-02-04 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_product_delete_uploadproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='addproduct',
        ),
    ]
