# Generated by Django 5.1.4 on 2025-02-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_database'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('productprice', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
