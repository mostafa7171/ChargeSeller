# Generated by Django 3.2.13 on 2023-07-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargesaletransaction',
            name='mobile',
            field=models.CharField(default='', max_length=11),
        ),
    ]
