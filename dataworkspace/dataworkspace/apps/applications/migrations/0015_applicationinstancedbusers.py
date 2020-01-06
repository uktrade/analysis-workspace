# Generated by Django 2.2.8 on 2019-12-13 12:11

import uuid
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('applications', '0014_auto_20191211_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationInstanceDbUsers',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('db_username', models.CharField(max_length=256)),
                (
                    'application_instance',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='applications.ApplicationInstance',
                    ),
                ),
                (
                    'db',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='core.Database'
                    ),
                ),
            ],
            options={'abstract': False},
        )
    ]