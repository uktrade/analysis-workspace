# Generated by Django 3.0.5 on 2020-06-09 21:16

from django.db import migrations


def copy_permissions(apps, schema_editor):
    VisualisationCatalogueItem = apps.get_model(
        'datasets', 'VisualisationCatalogueItem'
    )

    visualisations = VisualisationCatalogueItem.objects.all()
    for visualisation in visualisations:
        visualisation.user_access_type = (
            visualisation.visualisation_template.user_access_type
        )
        visualisation.save()


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [('datasets', '0047_auto_20200609_1027')]

    operations = [migrations.RunPython(code=copy_permissions, reverse_code=noop)]