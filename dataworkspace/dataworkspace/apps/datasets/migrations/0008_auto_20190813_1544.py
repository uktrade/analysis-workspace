# Generated by Django 2.2.3 on 2019-08-13 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0007_auto_20190813_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencedatasetfield',
            name='column_name',
            field=models.CharField(
                help_text='Descriptive column name for the field - Column name will be '
                          'used in external databases',
                max_length=255,
                null=False,
                validators=[
                    django.core.validators.RegexValidator(
                        message='Column names must start with a letter and contain only '
                                'letters, numbers, underscores and full stops.',
                        regex='^[a-zA-Z][a-zA-Z0-9_\\.]*$'
                    )
                ]
            ),
        ),
    ]