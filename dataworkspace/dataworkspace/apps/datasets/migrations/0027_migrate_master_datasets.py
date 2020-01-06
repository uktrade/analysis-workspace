# Generated by Django 2.2.4 on 2019-12-06 13:41

from django.db import migrations

from dataworkspace.apps.datasets.models import DataSet


def migrate_data_cut_to_master_dataset(apps, _):
    model = apps.get_model('datasets', 'DataCutDataset')
    for dataset in model.objects.filter(sourcetable__isnull=False):
        dataset.type = DataSet.TYPE_MASTER_DATASET
        dataset.save()


class Migration(migrations.Migration):

    dependencies = [('datasets', '0026_add_dataset_type_proxy_models')]

    operations = [
        migrations.RunPython(
            migrate_data_cut_to_master_dataset, reverse_code=migrations.RunPython.noop
        )
    ]