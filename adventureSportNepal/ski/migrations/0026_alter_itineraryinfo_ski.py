# Generated by Django 3.2.5 on 2021-07-27 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ski', '0025_auto_20210727_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itineraryinfo',
            name='ski',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraryinfo', to='ski.ski'),
        ),
    ]