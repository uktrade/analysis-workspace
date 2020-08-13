# Generated by Django 3.0.8 on 2020-08-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0010_auto_20200724_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtemplate',
            name='application_help_link',
            field=models.URLField(
                blank=True,
                help_text='A link to a Help Centre article that explains how to use this tool.',
                max_length=1024,
            ),
        ),
        migrations.AddField(
            model_name='applicationtemplate',
            name='application_summary',
            field=models.CharField(
                blank=True,
                help_text='A few sentences describing the high-level features of this tool.',
                max_length=255,
            ),
        ),
    ]