# Generated by Django 2.2.4 on 2019-08-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20190827_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtemplate',
            name='host_pattern',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
