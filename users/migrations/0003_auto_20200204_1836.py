# Generated by Django 3.0.3 on 2020-02-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phoneNumber',
            field=models.CharField(default='0', max_length=20),
        ),
    ]