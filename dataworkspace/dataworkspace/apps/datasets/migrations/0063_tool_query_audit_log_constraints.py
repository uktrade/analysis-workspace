# Generated by Django 3.0.8 on 2020-12-14 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0062_visualisationcatalogueitem_tags'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='toolqueryauditlog',
            unique_together={('rolename', 'query_sql', 'timestamp')},
        ),
    ]
