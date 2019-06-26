# Generated by Django 2.1.2 on 2019-06-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_privilage_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='user_access_type',
            field=models.CharField(choices=[('REQUIRES_AUTHENTICATION', 'Requires authentication'), ('REQUIRES_AUTHORIZATION', 'Requires authorization')], default='REQUIRES_AUTHORIZATION', max_length=64),
        ),
    ]
