# Generated by Django 3.2 on 2021-04-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrels',
            name='Location',
            field=models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('Other', 'Other')], max_length=15, null=True),
        ),
    ]
