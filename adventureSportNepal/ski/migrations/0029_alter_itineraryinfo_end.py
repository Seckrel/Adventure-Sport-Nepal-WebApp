# Generated by Django 3.2.5 on 2021-07-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0028_auto_20210729_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraryinfo',
            name='end',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='End Day'),
        ),
    ]
